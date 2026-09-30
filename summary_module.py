import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    raise ValueError("GEMINI_API_KEY not found. Please add your Gemini API key to the .env file.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.
Summarize the following educational content.
Content:
{text}
Requirements:
- Keep the important concepts.
- Remove unnecessary repetition.
- Use simple student-friendly language.
- Use bullet points where appropriate.
- Preserve important facts, definitions and examples.
"""
    try:
        response = model.generate_content(prompt)
        return response.text if response.text else "Sorry, I could not generate the summary."
    except Exception as e:
        return f"Error while generating summary: {str(e)}"
