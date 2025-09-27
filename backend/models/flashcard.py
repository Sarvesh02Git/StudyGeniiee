# backend/models/flashcard.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship # Add this import
from services.database import Base


class Flashcard(Base):
    __tablename__ = "flashcards"
    
    flashcard_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey("study_materials.material_id"), nullable=False)
    front_text = Column(String(1000), nullable=False)
    back_text = Column(String(1000), nullable=False)
    last_reviewed_date = Column(DateTime(timezone=True))
    next_review_date = Column(DateTime(timezone=True))
    repetition_count = Column(Integer, default=0)

    # Define relationship to study_material here
    study_material = relationship("StudyMaterial", back_populates="flashcards")
