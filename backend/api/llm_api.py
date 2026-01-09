# backend/api/llm_api.py


import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You create clean, concise educational summaries."
            },
            {
                "role": "user",
                "content": (
                    "Summarize the following content into 5–7 clear bullet points. "
                    "Each bullet must be a complete sentence. "
                    "Do not leave any sentence unfinished.\n\n"
                    f"{text}"
                )
            }
        ],
        temperature=0.2,
        max_tokens=500
    )
    return response.choices[0].message.content
