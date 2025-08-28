from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from services.database import Base
from sqlalchemy.orm import relationship

class Quiz(Base):
    __tablename__ = "quizzes"
    
    quiz_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey("study_materials.material_id"), nullable=False)
    score = Column(Integer)
    completion_date = Column(DateTime(timezone=True))
    
    questions = relationship("QuizQuestion", back_populates="quiz")
