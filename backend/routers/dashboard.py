# backend/routers/dashboard.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from services.database import get_db
from models.user import User
from models.document import Document
from models.quiz import Quiz
from models.quiz_question import QuizQuestion

router = APIRouter()

@router.get("/progress/{user_id}")
async def get_user_progress(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Fetches the user's overall study progress.
    """
    # Check if user exists
    user_exists = await db.scalar(select(User).where(User.user_id == user_id))
    if not user_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    # Get total documents uploaded
    total_docs_uploaded = await db.scalar(select(func.count(Document.document_id)).where(Document.user_id == user_id))

    # Get total quizzes completed
    quizzes_completed = await db.scalar(select(func.count(Quiz.quiz_id)).join(Document).where(Document.user_id == user_id))

    # Get average score across all quizzes
    avg_score_result = await db.execute(
        select(func.avg(Quiz.score)).join(Document).where(Document.user_id == user_id)
    )
    avg_score = avg_score_result.scalar()

    return {
        "user_id": user_id,
        "total_documents": total_docs_uploaded,
        "quizzes_completed": quizzes_completed,
        "average_score": avg_score if avg_score is not None else 0
    }

@router.get("/quizzes/document/{document_id}")
async def get_quizzes_for_document(document_id: int, db: AsyncSession = Depends(get_db)):
    """
    Fetches a list of quizzes for a specific document.
    """
    quiz_results = await db.execute(
        select(Quiz.quiz_id, Quiz.score, Quiz.completion_date).join(Document).where(Document.document_id == document_id)
    )
    quizzes = quiz_results.all()

    if not quizzes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No quizzes found for this document.")
    
    # You can return the data as a list of dictionaries for the frontend
    return [
        {"quiz_id": q.quiz_id, "score": q.score, "completion_date": q.completion_date} for q in quizzes
    ]