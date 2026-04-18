from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def call_llm(prompt):
    res = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content