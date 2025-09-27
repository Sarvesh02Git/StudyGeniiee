# backend/models/quiz.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship # Add this import
from services.database import Base


class Quiz(Base):
    __tablename__ = "quizzes"
    
    quiz_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey("study_materials.material_id"), nullable=False)
    score = Column(Integer)
    completion_date = Column(DateTime(timezone=True))
    
    # Define relationships here
    questions = relationship(
        "QuizQuestion", 
        back_populates="quiz", 
        cascade="all, delete-orphan"
    )
    study_material = relationship("StudyMaterial", back_populates="quizzes")
