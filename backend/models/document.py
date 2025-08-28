# backend/models/document.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from services.database import Base

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    title = Column(String(255), nullable=False)
    upload_date = Column(DateTime(timezone=True), server_default=func.now())
    file_path = Column(String(255), nullable=False)
    document_type = Column(String(50))
    
    user = relationship("User", back_populates="documents")