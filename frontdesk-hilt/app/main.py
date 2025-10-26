from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import Base, engine, get_db
from app.services.agent import process_customer_question
from app.services.help_request import resolve_request
from app.services.knowledge_base import get_all_knowledge

app = FastAPI(title="Frontdesk Human-in-the-Loop AI")

# Create DB tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Frontdesk AI Human-in-the-Loop System is running 🚀"}


@app.post("/api/call")
def customer_call(question: str, db: Session = Depends(get_db)):
    """
    Simulate a customer asking a question.
    The AI checks if it knows the answer, otherwise escalates.
    """
    return process_customer_question(db, question)


@app.post("/api/supervisor/respond")
def supervisor_response(request_id: str, answer: str, db: Session = Depends(get_db)):
    """
    Supervisor submits an answer to a pending help request.
    """
    return resolve_request(db, request_id, answer)


@app.get("/api/knowledge")
def show_knowledge(db: Session = Depends(get_db)):
    """
    Show all learned answers.
    """
    return get_all_knowledge(db)
