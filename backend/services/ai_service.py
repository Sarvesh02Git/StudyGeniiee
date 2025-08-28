import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz_and_flashcards(text: str):
    """
    Generates a quiz and flashcards from the provided text using an LLM.
    """
    try:
        # Prompt for quiz generation
        quiz_prompt = (
            f"From the following text, generate a JSON object containing a list of 5 "
            f"multiple-choice questions. Each question should have 'question', 'options' (an array of strings), "
            f"and 'correct_answer' (one of the options). The text is:\n\n{text}"
        )
        
        # Prompt for flashcard generation
        flashcard_prompt = (
            f"From the following text, generate a JSON object containing a list of 10 "
            f"flashcards. Each flashcard should have 'front' and 'back' fields. "
            f"The text is:\n\n{text}"
        )
        
        # Call the OpenAI API for both prompts in parallel (if possible, or sequentially)
        quiz_response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=quiz_prompt,
            max_tokens=512
        )
        
        flashcard_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=flashcard_prompt,
            max_tokens=512
        )
        
        return {
            "quizzes": quiz_response.choices[0].text.strip(),
            "flashcards": flashcard_response.choices[0].text.strip()
        }
        
    except Exception as e:
        print(f"Error calling AI service: {e}")
        return {"quizzes": "{}", "flashcards": "{}"}