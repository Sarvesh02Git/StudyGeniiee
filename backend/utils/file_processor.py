# backend/utils/file_processor.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from fastapi import HTTPException
import io

def extract_text_from_file(file_content: bytes, filename: str) -> str:
    """
    Extracts text from a PDF or image file.
    """
    if filename.lower().endswith('.pdf'):
        return _extract_text_from_pdf(file_content)
    elif filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return _extract_text_from_image(file_content)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

def _extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    text = ""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")

def _extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # Note: You may need to specify the path to your Tesseract executable
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image with OCR: {e}")# backend/utils/file_processor.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from fastapi import HTTPException
import io

def extract_text_from_file(file_content: bytes, filename: str) -> str:
    """
    Extracts text from a PDF or image file.
    """
    if filename.lower().endswith('.pdf'):
        return _extract_text_from_pdf(file_content)
    elif filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return _extract_text_from_image(file_content)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

def _extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    text = ""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")

def _extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # Note: You may need to specify the path to your Tesseract executable
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image with OCR: {e}")