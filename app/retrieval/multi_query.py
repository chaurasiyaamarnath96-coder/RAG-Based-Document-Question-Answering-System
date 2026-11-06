from app.retrieval.query_expansion import (
    expand_query
)

from app.retrieval.retrieval_service import (
    RetrievalService
)


def multi_query_retrieval(
        query: str,
        session_id
):
    print(f"Original query: {query}")
    queries = [query]
    queries = expand_query(
        queries
    )
    print(queries)

    queries.append(
        query
    )

    all_results = []

    for q in queries:

        results = (
            RetrievalService
            .retrieve(
                q,
                session_id)
        )
        print(f"Results for query '{q}': {results}")
        print(f"Number of results for query '{q}': {len(results)}")

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