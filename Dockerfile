FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app
ENV GOOGLE_CLOUD_PROJECT=1051385917818

EXPOSE 8080

CMD ["uvicorn", "src.gateway.main:app", "--host", "0.0.0.0", "--port", "8080"]
