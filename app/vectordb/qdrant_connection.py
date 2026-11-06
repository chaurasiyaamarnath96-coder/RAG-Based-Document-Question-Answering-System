from qdrant_client import QdrantClient
import os
client = QdrantClient(
    host = os.getenv("QDRANT_HOST", 'localhost'),
    port = int(os.getenv("QDRANT_PORT", 6333)),
    check_compatibility=False
)
