from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: int
    code: int
    answer: str
    question: str


class CreateQuestionSchema(BaseModel):
    code: int
    answer: str
    question: str