from app.llm.gemma_client import (
    generate_answer
)

def expand_query(
        query
):
    prompt = f"""
Generate 3 alternative search queries for:

{query}

Return one query per line.
"""

    result = generate_answer(
        prompt
    )
    queries = [
        q.strip() for q in result.split(
            "\n"
        )
        if q.strip()
    ]
    return queries