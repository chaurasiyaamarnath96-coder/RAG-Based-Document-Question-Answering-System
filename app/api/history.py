from fastapi import APIRouter
from app.db.database import sessionLocal
from app.db.models import ChatSession

from app.memory.conversation_memory import(
    get_history
)

from app.memory.conversation_memory import (
    get_sessions
)
from app.services.session_service import (
    rename_session
)

router = APIRouter(
    prefix="/history",
    tags = ["History"]
)

@router.get("/")
async def chat_history(
    session_id: str

):
    return {
        "session_id": session_id,
        "messages": get_history(
            session_id
        )
    }

@router.put("/rename")
async def rename_chat(
        session_id: str,

        title: str
):

    rename_session(
        session_id,
        title
    )

    return {
        "message":
        "updated"
    }
@router.get("/sessions")
async def get_sessions():

    db = sessionLocal()

    sessions = (
        db.query(ChatSession)
        .order_by(ChatSession.id.desc())
        .all()
    )

    result = [
        {
            "session_id": s.session_id,
            "title": s.title
        }
        for s in sessions
    ]

    db.close()

    return {
        "sessions": result
    }