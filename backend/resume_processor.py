from io import BytesIO
import pdfminer.high_level

def extract_resume_text(pdf_bytes: bytes) -> str:
    return pdfminer.high_level.extract_text(BytesIO(pdf_bytes))

