import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

API_URL = (
    "https://api.groq.com/openai/v1/chat/completions"
)

headers = {

    "Authorization":
        f"Bearer {GROQ_API_KEY}",

    "Content-Type":
        "application/json"
}


def call_llm(prompt):

    payload = {

        "model":
            "llama-3.1-8b-instant",

        "messages": [

            {
                "role": "user",

                "content": prompt
            }
        ],

        "temperature": 0.3,

        "max_tokens": 800
    }

    response = requests.post(

        API_URL,

        headers=headers,

        json=payload
    )

    data = response.json()

    try:

        return data[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]

    except Exception:

        return f"❌ LLM Error: {data}"