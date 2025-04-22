import openai

openai.api_key = "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"

async def get_openai_response(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # можешь использовать любую модель гпт
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"
