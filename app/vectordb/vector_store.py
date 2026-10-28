import uuid
from qdrant_client.models import (
    PointStruct
)

from app.vectordb.qdrant_connection import client

def store_chunks(
        chunks,
        filename,
        pages
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
                    "pages": chunk["page"]
                }
            )
        )
    client.upsert(
        collection_name="pdf_chunks",
        points= points
    )