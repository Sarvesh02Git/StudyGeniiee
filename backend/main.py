import logging
import logging.config
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
# Import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, content, dashboard
from services.database import create_db_and_tables
from utils.logger_config import setup_logging

# ADD THESE IMPORTS to ensure SQLAlchemy discovers the models
from models import user, document, study_material, flashcard, quiz, quiz_question 


# Set up logging at the application's entry point
setup_logging()
logger = logging.getLogger("app")

# --- Application Lifecycle Events ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    """
    logger.info("Application starting up...")
    
    # Run database table creation on startup
    await create_db_and_tables()
    logger.info("Database tables created or already exist.")
    
    yield  # The app runs until this point
    
    # This code runs on application shutdown
    logger.info("Application shutting down...")


# --- FastAPI Application Instance ---
app = FastAPI(
    title="StudyGenie API",
    description="API for a personalized study guide generator.",
    version="1.0.0",
    lifespan=lifespan  # Link the lifespan manager
)

# --- CORS Configuration ---
# Define the origins that are allowed to make requests
origins = [
    "http://localhost",
    "http://localhost:4200",  # Your Angular frontend's URL
    # Add any other origins where your frontend might be hosted (e.g., your IP address)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)
# --- End CORS Configuration ---


# --- Include Routers ---
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(content.router, prefix="/api/content", tags=["Content Generation"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard & Progress"])


# --- Root Endpoint (for health check) ---
@app.get("/")
def read_root():
    """
    Returns a simple message to indicate the API is running.
    """
    return {"message": "Welcome to StudyGenie API!"}
