def build_prompt(
        query,
        contexts,
        history
):

    context_text = "\n\n".join(
        contexts
    )
    if not context_text:
        return {
            "answer": "I could not find this information in the uploaded documents.",
            "context": "No context available.",
            "source": []
        }

    history_text = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in history
        ]
    )

    prompt = f"""
You are a document assistant.

Use ONLY the provided context.

If the answer is not found in the context, respond exactly:

"I could not find this information in the uploaded documents."

Do not use your own knowledge.

Conversation History:
{history_text}

Context:
{context_text}

Question:
{query}

Answer:
"""

    return prompt