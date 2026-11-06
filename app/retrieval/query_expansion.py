from app.llm.gemma_client import (
    generate_answer
)

def expand_query(query):

    prompt = f"""
You are a search query expansion assistant.

Original Query:
{query}

Generate 3 alternative search queries that preserve the EXACT meaning.

Rules:
- Keep the same intent.
- Use synonyms only.
- Do not invent new topics.
- Do not generate biography requests.
- Do not generate politician/public figure queries.
- Keep queries short.

Return ONLY the queries.
One query per line.
"""

    result = generate_answer(prompt)

    queries = [
        q.strip()
        for q in result.split("\n")
        if q.strip()
    ]

    return queries