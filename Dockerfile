FROM python:3.7-alpine

COPY .env .env

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main/main.py"]
