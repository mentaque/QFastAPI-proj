import requests

from crud import get_question_by_code


def get_data(count, db):
    url = f"https://jservice.io/api/random?count={count}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        items = []
        for item in data:
            try:
                get_question_by_code(item["id"], db)
                items.extend(get_data(1, db))
            except:
                item_id = item["id"]
                item_answer = item["answer"]
                item_question = item["question"]
                items.append((item_id, item_answer, item_question))
        return items
    else:
        return None
