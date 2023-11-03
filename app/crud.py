from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Question


def get_question_by_code(code: int, db: Session):
    question = db.query(Question).filter(Question.code == code).first()
    if not question:
        raise HTTPException(status_code=404, detail="Запись не найдена в бд")
    return question


def get_db_questions(skip: int, limit: int, db: Session):
    return db.query(Question).offset(skip).limit(limit).all()


def create_questions(code: int, answer: str, question: str, db: Session):
    try:
        created_question = Question(code=code, answer=answer, question=question)
        db.add(created_question)
        db.commit()
        return created_question
    except:
        raise HTTPException(status_code=400, detail="Поле 'code' должно быть уникальным")


def delete_db_question(code: int, db: Session):
    try:
        question = get_question_by_code(code, db=db)
        db.delete(question)
        db.commit()
        return question
    except:
        raise HTTPException(status_code=404, detail="Запись не найдена в бд")
