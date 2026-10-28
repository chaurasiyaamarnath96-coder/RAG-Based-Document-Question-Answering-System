from app.retrieval.dense_search import (
    search
)

from app.retrieval.bm25_search import (
    bm25search
)

from app.retrieval.fusion import (
    reciprocal_rank_fusion
)


class RetrievalService:

    @staticmethod
    def retrieve(
            query
    ):

        dense_results = (
            search(
                query
            )
        )

        bm25_results = (
            bm25search(
                query
            )
        )

        hybrid_results = (
            reciprocal_rank_fusion(
                dense_results,
                bm25_results
            )
        )

        return hybrid_results