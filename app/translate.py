from googletrans import Translator
from sqlalchemy.orm import Session

from crud import get_question_by_code

translator = Translator()


def translate(code, db: Session):
    question = get_question_by_code(code=code, db=db)
    translated = {
        'код': question.code,
        'Вопрос': translator.translate(question.question, src='en', dest='ru').text,
        'Ответ': translator.translate(question.answer, src='en', dest='ru').text
    }
    return translated
