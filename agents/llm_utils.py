import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if API_KEY:
    genai.configure(api_key=API_KEY)


def trim_text(text, max_chars=14000):
    if not text:
        return ""
    text = str(text)
    return text[:max_chars]


def call_gemini(prompt, temperature=0.3, max_retries=2):
    if not API_KEY:
        return "Error: GEMINI_API_KEY not found. Please add it to your .env file."

    model = genai.GenerativeModel(
        MODEL_NAME,
        generation_config={
            "temperature": temperature,
            "top_p": 0.9,
            "top_k": 40,
        },
    )

    last_error = None

    for attempt in range(max_retries + 1):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            last_error = e
            time.sleep(2)

    return f"""
## API Error

The agent could not generate output because the Gemini API request failed.

**Reason:** {last_error}

Please check:
- API key
- Google AI Studio project access
- quota limits
- billing status
"""