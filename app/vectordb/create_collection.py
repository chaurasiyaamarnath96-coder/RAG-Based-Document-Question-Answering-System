# create_collection.py

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance
)

client = QdrantClient(
    host="localhost",
    port=6333,
    check_compatibility=False
)

client.create_collection(
    collection_name="pdf_chunks",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

print("Collection Created Successfully")