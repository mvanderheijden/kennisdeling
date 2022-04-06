FROM python:3.10-slim

ENV PORT 8000
ENV PYTHONUNBUFFERED 1

WORKDIR app
COPY main.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn --reload main:app --host 0.0.0.0 --port $PORT

# docker build -t excercise4 .
# docker run --name excercise4 -e PORT=8080 -p 8080:8080 -v ~/gitrepos/kennisdeling/docker/exercise4:/app excercise4

