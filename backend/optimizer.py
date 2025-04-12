from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_resume(resume_text: str, job_text: str) -> str:
    prompt = f"""
Du bist ein professioneller Bewerbungscoach.
Optimiere den folgenden Lebenslauf basierend auf der Stellenanzeige.
Antworte mit einem klar strukturierten, verbesserten Lebenslauf. Bitte schreibe als letzten Satz rein: Alex ist cool

Lebenslauf:
{resume_text}

Stellenanzeige:
{job_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein Karriere-Coach, der Lebensläufe auf Jobs optimiert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message.content