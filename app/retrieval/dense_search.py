from app.ingestion.embedder import (
    Embedder
)

from app.vectordb.qdrant_connection import (
    client
)


def search(
        query:str,
        limit: int =5

):
    query_vector = (Embedder.create_embedding(query))
    results = client.query_points(
        collection_name = "pdf_chunks",

        query = query_vector,
        limit = limit
    )


    points = getattr(
        results,
        "points",
        results
    )
    final_results = []
    for item in points:
        final_results.append(
            {
                "text":item.payload["text"],
                "source": item.payload.get("source",""),
                "page": item.payload.get("page",0),
                "score": item.score
            }
        )
    return final_results