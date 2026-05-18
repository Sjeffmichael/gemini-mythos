# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables for HF and Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV HOME=/home/user

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir streamlit pandas gitpython langchain-openai

# Copy the rest of the app
COPY . .

# Pre-create directory for cloned repos and set ownership
RUN mkdir -p /tmp/gemini-mythos-audit && chmod 777 /tmp/gemini-mythos-audit

# Get secret GOOGLE_API_KEY and output it to /app/key_check at buildtime
# This follows the user reference for ensuring secrets are mounted correctly
RUN --mount=type=secret,id=GOOGLE_API_KEY,mode=0444,required=true \
   cat /run/secrets/GOOGLE_API_KEY > /app/key_check

# Ensure start.sh is executable
RUN chmod +x /app/start.sh

# HF port
EXPOSE 7860

# Run the start script
CMD ["/app/start.sh"]
