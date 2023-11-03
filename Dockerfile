FROM tiangolo/uvicorn-gunicorn:python3.10

COPY app/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app