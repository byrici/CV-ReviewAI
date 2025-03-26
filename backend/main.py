from fastapi import FastAPI, UploadFile, File
import pdfminer.high_level

app = FastAPI()

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = pdfminer.high_level.extract_text_from_io(content)
    return {"text": text}

# Starte den Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
