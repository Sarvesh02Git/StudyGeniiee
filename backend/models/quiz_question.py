from sqlalchemy import Column, Integer, String, ForeignKey
from services.database import Base
from sqlalchemy.orm import relationship

class QuizQuestion(Base):
    __tablename__ = "quiz_questions"
    
    question_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.quiz_id"), nullable=False)
    question_text = Column(String(1000), nullable=False)
    option_A = Column(String(500))
    option_B = Column(String(500))
    option_C = Column(String(500))
    option_D = Column(String(500))
    correct_option = Column(String(10), nullable=False)
    
    quiz = relationship("Quiz", back_populates="questions")