def normal_rerank(
        results,
        top_k: int = 10
):

    ranked_results = sorted(
        results,
        key=lambda x:
        x.get(
            "rrf_score",
            0
        ),
        reverse=True
    )

    return ranked_results[:top_k]