import ollama


def generate_answer(
        prompt: str
):

    response = ollama.chat(
        model="gemma2:2b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]