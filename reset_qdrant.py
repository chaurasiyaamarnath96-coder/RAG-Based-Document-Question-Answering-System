from app.vectordb.qdrant_connection import client

client.delete_collection(
    collection_name="pdf_chunks"
)

print("Collection deleted")