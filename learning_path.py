import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    raise ValueError("GEMINI_API_KEY not found. Please add your Gemini API key to the .env file.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def recommend_learning_path(topic: str) -> str:
    prompt = f"""
You are EduGenie, an AI learning assistant.
Create a personalized learning path for the following topic:
Topic:
{topic}
Organize the learning path from beginner to advanced.
Include:
1. Beginner concepts
2. Intermediate concepts
3. Advanced concepts
4. Suggested practice activities
5. Useful learning resources or resource types
6. A recommended order for studying the concepts
Keep the explanation simple and student-friendly.
"""
    try:
        response = model.generate_content(prompt)
        return response.text if response.text else "Sorry, I could not generate a learning path."
    except Exception as e:
        return f"Error while generating learning path: {str(e)}"
