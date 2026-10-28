from app.retrieval.retrieval_service import (
    RetrievalService
)
from app.llm.prompt_builder import (
    build_prompt

)

from app.llm.gemma_client import (
    generate_answer
)
from app.retrieval.cross_encoder_reranker import (
    rerank
)




from app.memory.conversation_memory import (
    add_message,
    get_history
)
from app.retrieval.multi_query import (
        multi_query_retrieval
    )

def ask(
        query: str,
        session_id: str
):
    
    chunks = multi_query_retrieval(
        query
    )

    chunks = rerank(
        query,
        chunks
    )
    contexts = [
        chunk["text"]
        for chunk in chunks
    ]
    history = get_history(
        session_id
    )

    prompt = build_prompt(
        query,
        contexts,
        history
    )
    answer = generate_answer(
        prompt
    )
    add_message(
        session_id,
        "user",
        query
    )

    add_message(
        session_id,
        "assistant",
        answer
    )
    unique_sources = []

    seen = set()

    for chunk in chunks:

        key = (
            str(chunk.get("source", "")),
            str(chunk.get("page",0))
        )

        if key not in seen:

            seen.add(
                key
            )

            unique_sources.append(
                {
                    "file":
                    chunk["source"],

                    "page":
                    chunk["page"]
                }
            )
    return {
        "answer":answer,
        "source": unique_sources
    }