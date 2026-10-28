from sentence_transformers import (
    CrossEncoder
)

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(
        query,
        results,
        top_k=5
):

    if not results:
        return []

    pairs = [

        (
            query,
            item.get(
                "text",
                ""
            )
        )

        for item in results
    ]

    scores = model.predict(
        pairs
    )

    for item, score in zip(
            results,
            scores
    ):

        item[
            "cross_score"
        ] = float(score)

    results.sort(
        key=lambda x:
        x["cross_score"],
        reverse=True
    )

    return results[:top_k]