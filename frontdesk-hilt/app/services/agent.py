from sqlalchemy.orm import Session
from app.models import HelpRequest
from app.services.knowledge_base import find_answer, add_knowledge
from app.services.help_request import create_help_request
from app.services.notify import notify_supervisor

def process_customer_question(db: Session, question: str):
    # Step 1: Check knowledge base
    kb_answer = find_answer(db, question)
    if kb_answer:
        return {"known": True, "answer": kb_answer.answer}

    # Step 2: Escalate to human supervisor
    help_request = create_help_request(db, question)
    notify_supervisor(help_request)
    return {
        "known": False,
        "message": "Let me check with my supervisor and get back to you.",
        "help_request_id": help_request.id,
    }
