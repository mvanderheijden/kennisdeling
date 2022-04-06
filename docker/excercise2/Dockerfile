FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR app
COPY main.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0

# docker build -t excercise2 .
# docker run --name excercise2 -p 8000:8000 excercise2
