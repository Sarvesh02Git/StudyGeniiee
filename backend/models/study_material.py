# backend/models/study_material.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from services.database import Base

class StudyMaterial(Base):
    __tablename__ = "study_materials"
    
    material_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    document_id = Column(Integer, ForeignKey("documents.document_id"), nullable=False)
    material_type = Column(String(50), nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())