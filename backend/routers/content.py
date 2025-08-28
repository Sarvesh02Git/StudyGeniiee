# backend/routers/content.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.database import get_db
from utils.file_processor import extract_text_from_file
from services.ai_service import generate_quiz_and_flashcards
from models.document import Document
from models.study_material import StudyMaterial
from models.quiz import Quiz
from models.quiz_question import QuizQuestion
from models.flashcard import Flashcard
import json
import os

router = APIRouter()

@router.post("/upload-and-generate")
async def upload_and_generate(file: UploadFile = File(...), user_id: int = 1, db: AsyncSession = Depends(get_db)):
    """
    Accepts a file, processes it, and generates study materials.
    """
    try:
        # 1. Read file and extract text
        contents = await file.read()
        extracted_text = extract_text_from_file(contents, file.filename)
        
        # 2. Store document in the database
        new_doc = Document(user_id=user_id, title=file.filename, file_path=f"path/to/{file.filename}", document_type=file.content_type)
        db.add(new_doc)
        await db.commit()
        await db.refresh(new_doc)
        
        # 3. Generate content using the AI service
        generated_content = generate_quiz_and_flashcards(extracted_text)
        
        # 4. Save generated content to the database
        quiz_data = json.loads(generated_content["quizzes"])
        flashcard_data = json.loads(generated_content["flashcards"])

        # Create a new StudyMaterial entry for quizzes
        quiz_material = StudyMaterial(document_id=new_doc.document_id, material_type="quiz")
        db.add(quiz_material)
        await db.commit()
        await db.refresh(quiz_material)

        # Create a new Quiz entry
        new_quiz = Quiz(material_id=quiz_material.material_id, score=0)
        db.add(new_quiz)
        await db.commit()
        await db.refresh(new_quiz)
        
        for q in quiz_data:
            new_question = QuizQuestion(quiz_id=new_quiz.quiz_id, question_text=q['question'], option_A=q['options'][0], option_B=q['options'][1], option_C=q['options'][2], option_D=q['options'][3], correct_option=q['correct_answer'])
            db.add(new_question)
        
        # Create a new StudyMaterial entry for flashcards
        flashcard_material = StudyMaterial(document_id=new_doc.document_id, material_type="flashcard")
        db.add(flashcard_material)
        await db.commit()
        await db.refresh(flashcard_material)
        
        for f in flashcard_data:
            new_flashcard = Flashcard(material_id=flashcard_material.material_id, front_text=f['front'], back_text=f['back'])
            db.add(new_flashcard)
            
        await db.commit()
        
        return {"message": "Study materials generated and saved successfully!"}
        
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")