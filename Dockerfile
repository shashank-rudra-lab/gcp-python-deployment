FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if needed)
# RUN apt-get update && apt-get install -y --no-install-recommends ...

# Copy application files
COPY main.py .
COPY setup.py .

# Install package in editable mode
RUN pip install --no-cache-dir -e .

# Run the application
CMD ["run-app"]