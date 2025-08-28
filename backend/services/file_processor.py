import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from fastapi import HTTPException
import io

def process_file_to_text(file_content: bytes, filename: str):
    """
    Extracts text from a PDF or image file.
    """
    if filename.lower().endswith('.pdf'):
        return _extract_text_from_pdf(file_content)
    elif filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return _extract_text_from_image(file_content)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

def _extract_text_from_pdf(pdf_bytes: bytes):
    text = ""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")

def _extract_text_from_image(image_bytes: bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # Use a cloud OCR service like Google Vision AI for better accuracy
        # For a simple setup, Tesseract can be used locally
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as needed
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image with OCR: {e}")