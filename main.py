from fastapi import FastAPI
from app.vectordb.collection import create_collection
from app.api.search_api import router as search_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.core.constants import (
    PROJECT_NAME,
    VERSION,
    DESCRIPTION
)

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION
)

app.include_router(
    health_router
)
app.include_router(
    upload_router
)
app.include_router(
    search_router
)
app.include_router(
    chat_router
)


@app.get("/")
def root():

    return {
        "message":
        "Advanced RAG Running"
    }

