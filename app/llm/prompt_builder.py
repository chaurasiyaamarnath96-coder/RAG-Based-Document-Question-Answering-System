def build_prompt(
        query,
        contexts,
        history
):

    history_text = ""

    for item in history:

        history_text += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    context_text = "\n\n".join(
        contexts
    )

    return f"""
You are a helpful assistant.

Conversation History:

{history_text}

Context:

{context_text}

Question:

{query}

Answer:
"""