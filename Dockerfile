FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 80
CMD uvicorn app:app --port=5000 --host=0.0.0.0
