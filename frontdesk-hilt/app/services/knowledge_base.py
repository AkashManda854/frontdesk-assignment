from sqlalchemy.orm import Session
from app.models import KnowledgeBase

def find_answer(db: Session, question: str):
    return db.query(KnowledgeBase).filter(KnowledgeBase.question == question).first()

def add_knowledge(db: Session, question: str, answer: str):
    kb = KnowledgeBase(question=question, answer=answer)
    db.add(kb)
    db.commit()
    db.refresh(kb)
    return kb

def get_all_knowledge(db: Session):
    return db.query(KnowledgeBase).all()
