from fastapi import APIRouter
from app.db.database import sessionLocal
from app.db.models import ChatSession

from app.llm.rag_chain import ask
from fastapi.responses import (
    StreamingResponse
)

from app.llm.rag_chain import (
    stream_chat
)
router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
async def chat(
    session_id: str,
    query: str
):
    return ask(
        query,
        session_id
    )
@router.get("/stream")
async def stream_chat_api(
    session_id: str,
    query: str
):
    return StreamingResponse(

        stream_chat(
            query,
            session_id
    ),

    media_type=
    "text/plain"
    )