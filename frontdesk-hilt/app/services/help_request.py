from sqlalchemy.orm import Session
from app.models import HelpRequest
from datetime import datetime
from app.services.knowledge_base import add_knowledge
from app.services.notify import notify_customer

def create_help_request(db: Session, question: str):
    req = HelpRequest(question=question)
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

def resolve_request(db: Session, request_id: str, answer: str):
    req = db.query(HelpRequest).filter(HelpRequest.id == request_id).first()
    if not req:
        return {"error": "Request not found"}

    req.status = "resolved"
    req.answer = answer
    req.resolved_at = datetime.utcnow()
    db.commit()

    # Add to knowledge base
    add_knowledge(db, req.question, answer)

    # Notify customer
    notify_customer(req)

    return {"message": "Request resolved and knowledge updated"}
