FROM python:3.13-slim

WORKDIR /app

# Ensure we have the latest pip
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies directly to speed up build and ensure they are present
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pydantic \
    google-cloud-dlp \
    google-cloud-aiplatform \
    google-cloud-discoveryengine \
    requests \
    google-cloud-storage \
    google-cloud-bigquery \
    vertexai \
    loguru

# Copy the entire build directory into /app
COPY . .

# Set the PYTHONPATH to include /app so 'src' is findable
ENV PYTHONPATH=/app
ENV GOOGLE_CLOUD_PROJECT=1051385917818

EXPOSE 8080

# Execute the root-level script directly
CMD ["python", "run_gateway.py"]
