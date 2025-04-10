from fastapi import FastAPI, UploadFile, File
import pdfminer.high_level
from io import BytesIO

app = FastAPI()

@app.post("/upload/")
async def pdf_to_text(file: UploadFile = File(...)):
    content = await file.read()
    text = pdfminer.high_level.extract_text(BytesIO(content))
    return {"text": text}



# Starte den Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
