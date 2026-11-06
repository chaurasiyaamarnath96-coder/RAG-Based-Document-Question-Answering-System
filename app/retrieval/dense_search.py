from app.ingestion.embedder import (
    Embedder
)

from app.vectordb.qdrant_connection import (
    client
)
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue 
)


def search(
        query:str,
        session_id: str,
        limit: int =5

):
    records, _ = client.scroll(
        collection_name="pdf_chunks",
        limit=5,
        with_payload=True
    )
    print("\n===== SAMPLE PAYLOADS =====")

    for record in records:

        print(record.payload)

        print("==========================\n")
    query_vector = (Embedder.create_embedding(query))
    query_filter = Filter(
        must=[
            FieldCondition(
                key = "session_id",
                match = MatchValue(
                    value = session_id
                )
            )
        ]
    )
    results = client.query_points(
        collection_name = "pdf_chunks",

        query = query_vector,
        query_filter=query_filter,
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