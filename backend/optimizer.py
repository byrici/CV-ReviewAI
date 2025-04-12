from openai import OpenAI
import os
from dotenv import load_dotenv
import base64

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔤 Für textbasierte Stellenanzeigen (PDF etc.)
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

# 🖼️ Für bildbasierte Stellenanzeigen (z. B. .jpg, .png)
def optimize_resume_with_image(resume_text: str, image_bytes: bytes, image_format: str) -> str:
    mime_type = "image/png" if image_format == "png" else "image/jpeg"
    base64_data = base64.b64encode(image_bytes).decode("utf-8")
    image_base64_url = f"data:{mime_type};base64,{base64_data}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein Karriere-Coach, der Lebensläufe auf Jobs optimiert."},
            {"role": "user", "content": "Hier ist mein Lebenslauf:\n" + resume_text},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Hier ist die Stellenanzeige als Bild. Bitte optimiere meinen Lebenslauf entsprechend."},
                    {"type": "image_url", "image_url": {"url": image_base64_url}}
                ]
            }
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message.content
