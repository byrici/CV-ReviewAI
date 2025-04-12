from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from resume_processor import extract_resume_text
from job_parser import extract_job_text
from optimizer import optimize_resume, optimize_resume_with_image
import filetype  # statt imghdr (Python 3.13 kompatibel)

app = FastAPI()

# CORS aktivieren, damit das Frontend (React) mit dem Backend kommunizieren darf
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    # PDF-Dateien als Bytes einlesen
    resume_bytes = await resume.read()
    job_bytes = await job_description.read()

    # Lebenslauf immer in Text umwandeln
    resume_text = extract_resume_text(resume_bytes)

    # Typ der Stellenanzeige erkennen (Bild oder PDF?)
    kind = filetype.guess(job_bytes)

    if kind and kind.mime.startswith("image/"):
        # 📸 Wenn Bild: direkt an GPT-4o übergeben
        image_format = kind.extension  # z. B. 'jpeg', 'png'
        optimized_resume = optimize_resume_with_image(resume_text, job_bytes, image_format)
    else:
        # 📄 Wenn PDF/Text: extrahiere Text wie bisher
        job_text = extract_job_text(job_bytes)
        optimized_resume = optimize_resume(resume_text, job_text)

    return {
        "optimized_resume": optimized_resume
    }

# Starte den Server direkt über `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
