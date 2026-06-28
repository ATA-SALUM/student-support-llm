import requests
from config import OLLAMA_URL, MODEL


def ask_llm(question):

    prompt = f"""
You are a University Student Support Assistant.

Answer only questions related to:

- Course registration
- Examination rules
- Library services
- ICT support
- Hostel application
- Fee payment
- Academic calendar
- Student conduct

If the question is unrelated to university services,
politely explain that you only answer university support questions.

Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]