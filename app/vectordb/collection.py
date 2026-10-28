from qdrant_client.models import (
    VectorParams,
    Distance
)
from app.vectordb.qdrant_connection import client

def create_collection():
    collections = client.get_collections()

    existing = [
        c.name for c in
          collections.collections
    ]

    if "pdf_chunks" not in existing:
        client.create_collection(
            collection_name= "pdf_chunks",
            vectors_config=VectorParams(size=384,
                                        distance=Distance.COSINE)
        )
        print("Collection Created")
    else:
        print("Collection Already Exists")




