# backend/routers/content.py
import asyncio
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from services.database import get_db
from pydantic import BaseModel
import shutil
import os

router = APIRouter()

# Placeholder for processed file metadata
class ProcessedFileResponse(BaseModel):
    message: str
    filename: str
    file_id: str

async def process_uploaded_file(file_path: str, user_id: int):
    """
    This is a background task to process the uploaded file.
    In the next steps, we will add AI logic here.
    """
    try:
        # Placeholder for actual file processing and AI generation logic
        print(f"Processing file: {file_path} for user: {user_id}")
        # ---
        # TODO: Implement text extraction (PyMuPDF, Tesseract)
        # TODO: Call GenAI model to create quizzes/flashcards
        # TODO: Store results in the database
        # ---
        # For now, just simulate a successful process
        await asyncio.sleep(5)  # Simulate a long-running task
        print(f"File {file_path} processed successfully.")
    except Exception as e:
        print(f"Failed to process file: {e}")
    finally:
        # Clean up the temporary file after processing
        os.remove(file_path)

@router.post("/upload", status_code=status.HTTP_202_ACCEPTED)
async def upload_document(
    file: UploadFile = File(...),
    user_id: int = 1, # A temporary user ID for testing
    background_tasks: BackgroundTasks = BackgroundTasks(),
    db: AsyncSession = Depends(get_db)
):
    """
    Accepts a document upload and starts a background task for processing.
    """
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No file selected.")

    # Create a secure file path for the temporary file
    upload_dir = "temp_uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)

    try:
        # Save the file to a temporary location
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Add the processing task to the background
        background_tasks.add_task(process_uploaded_file, file_path, user_id)

        return {
            "message": "File upload successful. Processing started in the background.",
            "filename": file.filename
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to save file: {e}")