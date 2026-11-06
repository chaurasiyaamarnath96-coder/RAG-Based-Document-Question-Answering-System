import uuid
import streamlit as st

from api import (
    ask_question,
    get_history,
    get_sessions,
    upload_pdf,
    rename_chat
)

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Advanced RAG",
    page_icon="🤖",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================

if "session_id" not in st.session_state:

    st.session_state.session_id = (
        f"session_{uuid.uuid4().hex[:8]}"
    )

if "messages" not in st.session_state:

    st.session_state.messages = []
if "editing" not in st.session_state:
    st.session_state.editing = None
# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("🤖 Advanced RAG")

    st.divider()

    # NEW CHAT

    if st.button(
        "➕ New Chat",
        use_container_width=True
    ):

        st.session_state.session_id = (
            f"session_{uuid.uuid4().hex[:8]}"
        )

        st.session_state.messages = []

        st.rerun()

    st.divider()

    # PDF UPLOAD

    st.subheader("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"],
        key="pdf_upload"
    )

    if uploaded_file:

        if st.button(
            "Upload PDF",
            use_container_width=True,
            key="upload_btn"
        ):

            with st.spinner(
                "Processing PDF..."
            ):

                result = upload_pdf(
                    uploaded_file,
                    st.session_state.session_id
                )

            if "error" in result:

                st.error(
                    result["error"]
                )

            else:

                st.success(
                    f"Uploaded: {uploaded_file.name}"
                )

                st.json(result)

    st.divider()

    # SESSIONS

    st.subheader("💬 Chats")

    sessions = get_sessions()
    st.sidebar.write("DEBUG:", sessions)

    sessions = sessions.get(
        "sessions",
        []
    )

    if sessions:

        for chat in sessions:

            session_id = chat["session_id"]
            title = chat["title"]

            col1, col2 = st.columns(
                [5, 1]
            )

            with col1:

                if st.button(
                    title,
                    key=f"chat_{session_id}",
                    use_container_width=True
                ):

                    st.session_state.session_id = (
                        session_id
                    )

                    history = get_history(
                        session_id
                    )

                    st.session_state.messages = (
                        history.get(
                            "messages",
                            []
                        )
                    )

                    st.rerun()

            with col2:

                if st.button(
                    "✏",
                    key=f"edit_{session_id}"
                ):

                    st.session_state.editing = (
                        session_id
                    )

            if (
                st.session_state.editing
                ==
                session_id
            ):

                new_name = st.text_input(
                    "Rename Chat",
                    value=title,
                    key=f"rename_{session_id}"
                )

                if st.button(
                    "Save",
                    key=f"save_{session_id}"
                ):

                    rename_chat(
                        session_id,
                        new_name
                    )

                    st.session_state.editing = None

                    st.rerun()

# ==================================
# MAIN SCREEN
# ==================================

st.title(
    "🤖 Advanced RAG Assistant"
)

st.info(
    f"Current Chat:{st.session_state.session_id}"
)

if not st.session_state.messages:

    try:

        history = get_history(
            st.session_state.session_id
        )

        st.session_state.messages = (
            history.get(
                "messages",
                []
            )
        )

    except:

        pass
# ==================================
# DISPLAY OLD MESSAGES
# ==================================

for message in (
        st.session_state.messages
):

    with st.chat_message(
            message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ==================================
# USER INPUT
# ==================================

prompt = st.chat_input(
    "Ask anything about your PDFs..."
)

if prompt:

    # SHOW USER MSG

    st.session_state.messages.append(
        {
            "role":
            "user",

            "content":
            prompt
        }
    )

    with st.chat_message(
            "user"
    ):

        st.markdown(
            prompt
        )

    # CALL BACKEND

    with st.chat_message(
            "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = ask_question(

                    st.session_state.session_id,

                    prompt
                )

                answer = response.get(
                    "answer",
                    "No answer returned."
                )

                sources = response.get(
                    "sources",
                    []
                )

            except Exception as e:

                answer = (
                    f"Error: {str(e)}"
                )

                sources = []

        st.markdown(
            answer
        )

        # SOURCES

        if sources:

            st.markdown(
                "### 📚 Sources"
            )

            for source in sources:

                if isinstance(
                        source,
                        dict
                ):

                    st.markdown(

                        f"- **{source.get('file','Unknown')}** "
                        f"(Page {source.get('page','?')})"

                    )

    # STORE ASSISTANT MSG

    st.session_state.messages.append(
        {
            "role":
            "assistant",

            "content":
            answer
        }
    )