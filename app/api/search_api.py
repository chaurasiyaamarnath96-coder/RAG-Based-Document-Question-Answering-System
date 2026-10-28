from fastapi import APIRouter

from app.retrieval.retrieval_service import RetrievalService

router = APIRouter(
    prefix="/search",
    tags = ["Search"]
)

@router.get("")
async def search_docs(
    query: str
):

    return RetrievalService.retrieve(query)
