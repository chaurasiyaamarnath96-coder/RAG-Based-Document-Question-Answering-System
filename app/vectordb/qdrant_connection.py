from qdrant_client import QdrantClient

client = QdrantClient(
    host = 'localhost',
    port= 6333,
    check_compatibility=False
)
