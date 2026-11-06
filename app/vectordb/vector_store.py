import uuid
from qdrant_client.models import (
    PointStruct
)

from app.vectordb.qdrant_connection import client

def store_chunks(
        chunks,
        filename,
        pages,
        session_id
):
    points = []

    for chunk in chunks:
        points.append(
            PointStruct(
                id=str(
                    uuid.uuid4()
                ),
                vector=chunk["embedding"],
                payload={
                    "text":chunk["text"],
                    "source":filename,
                    "pages": chunk["pages"],
                    "session_id":chunk["session_id"]

                }
            )
        )
    client.upsert(
        collection_name="pdf_chunks",
        points= points
    )