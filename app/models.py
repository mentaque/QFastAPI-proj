from sqlalchemy import Column, Integer, String

from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True, index=True)
    answer = Column(String)
    question = Column(String)


metadata = Base.metadata
