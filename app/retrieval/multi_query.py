from app.retrieval.query_expansion import (
    expand_query
)

from app.retrieval.retrieval_service import (
    RetrievalService
)


def multi_query_retrieval(
        query: str
):

    queries = expand_query(
        query
    )

    queries.append(
        query
    )

    all_results = []

    for q in queries:

        results = (
            RetrievalService
            .retrieve(q)
        )

        all_results.extend(
            results
        )

    seen = set()

    unique_results = []

    for item in all_results:

        text = item["text"]

        if text not in seen:

            seen.add(text)

            unique_results.append(
                item
            )

    return unique_results