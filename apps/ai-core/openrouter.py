import httpx
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-oss-20b:free"


async def ask_openrouter(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=20
        )
        print(f"OpenRouter status code: {response.status_code}")
        print(f"OpenRouter response text: {response.text}")

    if response.status_code != 200:
        raise Exception(
            f"OpenRouter returned status {response.status_code}: {response.text}")

    response.raise_for_status()
    content = response.json()
    return content["choices"][0]["message"]["content"]
