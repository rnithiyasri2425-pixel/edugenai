from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path

app = FastAPI(
    title="EduGenie - AI Learning Assistant",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/qa")
async def qa(question: str = Form(...)):
    try:
        question = question.strip()

        if not question:
            return {
                "error": "Please enter a question."
            }

        answer = answer_question(question)

        return {
            "answer": answer
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/explain")
async def explain(text: str = Form(...)):
    try:
        text = text.strip()

        if not text:
            return {
                "error": "Please enter a topic to explain."
            }

        explanation = explain_concept(text)

        return {
            "explanation": explanation
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/quiz")
async def quiz(topic: str = Form(...)):
    try:
        topic = topic.strip()

        if not topic:
            return {
                "error": "Please enter a topic for the quiz."
            }

        quiz_data = generate_quiz(topic)

        return {
            "quiz": quiz_data
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        text = text.strip()

        if not text:
            return {
                "error": "Please enter text to summarize."
            }

        summary = summarize_text(text)

        return {
            "summary": summary
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/learn/recommendations")
async def learning_recommendations(
    topic: str = Form(...),
    level: str = Form("Beginner")
):
    try:
        topic = topic.strip()
        level = level.strip()

        if not topic:
            return {
                "error": "Please enter a topic."
            }

        recommendations = recommend_learning_path(
            topic,
            level
        )

        return {
            "recommendations": recommendations
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "EduGenie server is running"
    }
