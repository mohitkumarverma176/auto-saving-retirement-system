# docker build -t auto-savings-retirement-system .

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 5477

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5477"]