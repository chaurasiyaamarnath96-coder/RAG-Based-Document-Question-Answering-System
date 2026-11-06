from app.retrieval.retrieval_service import (
    RetrievalService
)
from app.llm.prompt_builder import (
    build_prompt

)

from app.llm.gemma_client import (
    generate_answer
)
from app.retrieval.cross_encoder_reranker import (
    rerank
)




from app.memory.conversation_memory import (
    add_message,
    get_history
)
from app.retrieval.multi_query import (
        multi_query_retrieval

    )
from app.llm.gemma_client import (
    stream_answer
)
from app.db.database import sessionLocal
from app.db.models import ChatSession


def ask(
        query: str,
        session_id: str
):
    
    chunks = multi_query_retrieval(
        query,
        session_id
    )

    chunks = rerank(
        query,
        chunks
    )
    print(chunks)
    if not chunks:

        return {
            "answer":
            "I could not find this information in the uploaded documents.",

            "sources":[]
        }

    
    contexts = [
        chunk["text"]
        for chunk in chunks
    ]
    history = get_history(
        session_id
    )

    prompt = build_prompt(
        query,
        contexts,
        history
    )
    answer = generate_answer(
        prompt
    )
    add_message(
        session_id,
        "user",
        query
    )

    add_message(
        session_id,
        "assistant",
        answer
    )
    unique_sources = []

    seen = set()

    for chunk in chunks:

        key = (
            str(chunk.get("source", "")),
            str(chunk.get("page",0))
        )

        if key not in seen:

            seen.add(
                key
            )

            unique_sources.append(
                {
                    "file":
                    chunk["source"],

                    "pages":
                    chunk["page"]
                }
            )
    db = sessionLocal()

    existing_session = (
        db.query(ChatSession)
        .filter(
            ChatSession.session_id == session_id
        )
        .first()
    )

    if not existing_session:

        new_session = ChatSession(
            session_id=session_id,
            title=query[:50]
        )
        print(
        "CREATING SESSION:",
        session_id,
        query[:50]
    )
        db.add(new_session)
        db.commit()
        print("SESSION SAVED")

    db.close()
    return {
        "answer":answer,
        "source": unique_sources
    }


def stream_chat(
        query,
        session_id
):

    history = get_history(
        session_id
    )

    chunks = multi_query_retrieval(
        query,
        session_id
    )

    chunks = rerank(
        query,
        chunks
    )
    if not chunks:

        return {
            "answer":
            "I could not find this information in the uploaded documents.",

            "sources":[]
        }
    print("Chunks:", chunks[0])

    top_score = chunks[0].get(
        "cross_score",
        0
    )

    if top_score < 1:

        return {
            "answer":
            "I could not find this information in the uploaded documents.",

            "sources":[]
        }

    contexts = [

        chunk["text"]

        for chunk
        in chunks
    ]

    prompt = build_prompt(
        query,
        contexts,
        history
    )

    answer = ""

    for token in stream_answer(
            prompt
    ):

        answer += token

        yield token

    add_message(
        session_id,
        "user",
        query
    )

    add_message(
        session_id,
        "assistant",
        answer
    )
    db = sessionLocal()

    existing_session = (
        db.query(ChatSession)
        .filter(
            ChatSession.session_id == session_id
        )
        .first()
    )

    if not existing_session:

        new_session = ChatSession(
            session_id=session_id,
            title=query[:50]
        )

        db.add(new_session)
        db.commit()

    db.close()