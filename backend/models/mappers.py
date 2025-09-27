# backend/models/mapper.py
from sqlalchemy.orm import relationship


from .user import User
from .document import Document
from .study_material import StudyMaterial
from .flashcard import Flashcard
from .quiz import Quiz
from .quiz_question import QuizQuestion


User.documents = relationship("Document", back_populates="user", cascade="all, delete-orphan")


Document.user = relationship("User", back_populates="documents")

# A Document has many StudyMaterials
Document.study_materials = relationship("StudyMaterial", back_populates="document", cascade="all, delete-orphan")

# A StudyMaterial belongs to a Document
StudyMaterial.document = relationship("Document", back_populates="study_materials")

# A StudyMaterial has many Flashcards
StudyMaterial.flashcards = relationship("Flashcard", back_populates="study_material", cascade="all, delete-orphan")

# A Flashcard belongs to a StudyMaterial
Flashcard.study_material = relationship("StudyMaterial", back_populates="flashcards")

# A StudyMaterial has many Quizzes
StudyMaterial.quizzes = relationship("Quiz", back_populates="study_material", cascade="all, delete-orphan")

# A Quiz belongs to a StudyMaterial
Quiz.study_material = relationship("StudyMaterial", back_populates="quizzes")

# A Quiz has many QuizQuestions
Quiz.questions = relationship("QuizQuestion", back_populates="quiz", cascade="all, delete-orphan")

# A QuizQuestion belongs to a Quiz
QuizQuestion.quiz = relationship("Quiz", back_populates="questions")

# This file doesn't need to be imported directly, but it must be run
# or imported somewhere (like in database.py) to register the models.
