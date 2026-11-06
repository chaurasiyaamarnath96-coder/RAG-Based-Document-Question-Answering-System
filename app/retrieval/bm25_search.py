from rank_bm25 import BM25Okapi

from app.vectordb.qdrant_connection import client


def bm25search(
        query: str,
        session_id: str,
        limit: int = 5
):

    records, _ = client.scroll(
        collection_name="pdf_chunks",
        limit=1000,
        with_payload=True
    )

    documents = []

    for point in records:
        if point.payload.get(
            "session_id"
        ) != session_id:
            continue

        documents.append(
            {
                "text":
                point.payload["text"],

                "source":
                point.payload.get(
                    "source",
                    ""
                ),
                "pages":
                point.payload.get(
                    "pages",
                    0
                )
            }
        )
    if not documents:
        return []
    tokenized_docs = [

        doc["text"].split()

        for doc in documents
    ]

    bm25 = BM25Okapi(
        tokenized_docs
    )

    scores = bm25.get_scores(
        query.split()
    )

    results = []

    for idx, score in enumerate(
            scores
    ):

        results.append(
            {
                "text":
                documents[idx]["text"],

                "source":
                documents[idx]["source"],
                "pages": documents[idx]["pages"],

                "score":
                float(score)
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:limit]