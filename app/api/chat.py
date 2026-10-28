from fastapi import APIRouter

from app.llm.rag_chain import ask

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat(
    session_id: str,
    query: str
):
    return ask(
        query,
        session_id
    )