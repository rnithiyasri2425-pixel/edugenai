EduGenie - Google Gemini Powered Learning Assistant

1. Extract this ZIP.
2. Open the EduGenie folder in VS Code.
3. Open Terminal in VS Code.
4. Create virtual environment:
   python -m venv venv
5. Activate it on Windows:
   venv\Scripts\activate
6. Install dependencies:
   pip install -r requirements.txt
7. Open .env and replace YOUR_GEMINI_API_KEY_HERE with your Gemini API key.
8. Start the app:
   uvicorn main:app --reload
9. Open:
   http://127.0.0.1:8000

Swagger API docs:
http://127.0.0.1:8000/docs

Health check:
http://127.0.0.1:8000/health
