from app.memory.session_store import (
    chat_store
)


def add_message(
        session_id,
        role,
        content
):

    if session_id not in chat_store:

        chat_store[session_id] = []

    chat_store[session_id].append({
        "role": role,
        "content": content
    })


def get_history(
        session_id
):

    return chat_store.get(
        session_id,
        []
    )