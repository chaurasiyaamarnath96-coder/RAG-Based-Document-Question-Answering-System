def reciprocal_rank_fusion(
        dense_results,
        bm25_results,
        k=60
):

    fused_scores = {}

    metadata = {}

    for rank, item in enumerate(
            dense_results
    ):

        text = item["text"]

        metadata[text] = {
            "source":
            item.get(
                "source",
                ""
            ),

            "page":
            item.get(
                "page",
                0
            )
        }

        fused_scores[text] = (
            fused_scores.get(
                text,
                0
            )
            +
            1 / (k + rank + 1)
        )

    for rank, item in enumerate(
            bm25_results
    ):

        text = item["text"]

        if text not in metadata:

            metadata[text] = {
                "source":
                item.get(
                    "source",
                    ""
                ),

                "page":
                item.get(
                    "page",
                    0
                )
            }

        fused_scores[text] = (
            fused_scores.get(
                text,
                0
            )
            +
            1 / (k + rank + 1)
        )

    results = []

    for text, score in (
            fused_scores.items()
    ):

        results.append(
            {
                "text":
                text,

                "source":
                metadata[text][
                    "source"
                ],

                "page":
                metadata[text][
                    "page"
                ],

                "rrf_score":
                score
            }
        )

    results.sort(
        key=lambda x:
        x["rrf_score"],
        reverse=True
    )

    return results[:5]