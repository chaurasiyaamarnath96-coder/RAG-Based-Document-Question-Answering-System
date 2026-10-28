from app.vectordb.qdrant_connection import(
    client
)
info = client.get_collection(
    "pdf_chunks"
)

print(info)