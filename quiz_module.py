import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    raise ValueError("GEMINI_API_KEY not found. Please add your Gemini API key to the .env file.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(topic: str):
    prompt = f"""
You are EduGenie, an educational quiz generator.
Create exactly 3 multiple-choice questions about:
Topic:
{topic}
Each question must have exactly 4 options.
Return ONLY valid JSON using this structure:
{{
  "quiz": [
    {{"question": "Question 1", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_answer": "Option A"}},
    {{"question": "Question 2", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_answer": "Option B"}},
    {{"question": "Question 3", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_answer": "Option C"}}
  ]
}}
Do not add explanations outside the JSON.
"""
    try:
        response = model.generate_content(prompt)
        raw_text = response.text
        return json.loads(clean_json_block(raw_text))
    except json.JSONDecodeError:
        return {"error": "Gemini returned invalid quiz JSON.", "raw_response": raw_text if "raw_text" in locals() else ""}
    except Exception as e:
        return {"error": f"Error while generating quiz: {str(e)}"}
