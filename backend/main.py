from fastapi import FastAPI, UploadFile, File
from resume_processor import extract_resume_text
from job_parser import extract_job_text
from optimizer import optimize_resume

app = FastAPI()

@app.post("/analyze/")
async def analyze(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    resume_bytes = await resume.read()
    job_bytes = await job_description.read()

    resume_text = extract_resume_text(resume_bytes)
    job_text = extract_job_text(job_bytes)

    optimized_resume = optimize_resume(resume_text, job_text)

    return {
        "optimized_resume": optimized_resume
    }

# Starte den Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
