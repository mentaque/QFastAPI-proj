from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from crud import get_db_questions, create_questions, get_question_by_code, delete_db_question
from database import get_db
from models import Question
from get_data_from_api import get_data
from schemas import QuestionSchema, CreateQuestionSchema
from translate import translate

app = FastAPI()


@app.get("/get_questions/")
async def get_questions(q: int = 1, db: Session = Depends(get_db)) -> list[QuestionSchema]:
    data = get_data(q, db)
    questions = []
    for question in data:
        created_question = create_questions(code=question[0], answer=question[1], question=question[2], db=db)
        questions.append(created_question)
    return questions


@app.get("/get_db_questions")
async def read_db_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[QuestionSchema]:
    return get_db_questions(skip=skip, limit=limit, db=db)


@app.get("/get_db_question")
async def read_db_question(code: int, db: Session = Depends(get_db)) -> QuestionSchema:
    return get_question_by_code(code=code, db=db)


@app.post("/create_your_questions")
async def create_your_questions(question: CreateQuestionSchema, db: Session = Depends(get_db)) -> QuestionSchema:
    return create_questions(code=question.code, answer=question.answer, question=question.answer, db=db)


@app.delete("/delete_question")
async def delete_question(code: int, db: Session = Depends(get_db)) -> QuestionSchema:
    return delete_db_question(code=code, db=db)


@app.get("/translate_question_by_code")
async def translate_question_by_code(code: int, db: Session = Depends(get_db)):
    return translate(code=code, db=db)








