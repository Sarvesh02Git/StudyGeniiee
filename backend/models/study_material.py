# backend/models/study_material.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship # Add this import
from services.database import Base


class StudyMaterial(Base):
    __tablename__ = "study_materials"
    
    material_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    document_id = Column(Integer, ForeignKey("documents.document_id"), nullable=False)
    material_type = Column(String(50), nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())

    # Define relationship to document here
    document = relationship("Document", back_populates="study_materials")

    # Define relationships to flashcards and quizzes here
    flashcards = relationship(
        "Flashcard", 
        back_populates="study_material", 
        cascade="all, delete-orphan"
    )
    quizzes = relationship(
        "Quiz", 
        back_populates="study_material", 
        cascade="all, delete-orphan"
    )
