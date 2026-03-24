FROM python:3.10-slim

WORKDIR /app

COPY main.py .
COPY books/ books/

CMD ["python", "main.py"]
