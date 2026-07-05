# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install the required Google Cloud BigQuery library
RUN pip install --no-cache-dir google-cloud-bigquery

# Copy your Python script into the container
COPY bigquery_demo.py .

# Run the Python script when the container starts
CMD ["python", "bigquery_demo.py"]
