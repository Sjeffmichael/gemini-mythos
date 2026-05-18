# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir streamlit pandas gitpython langchain-openai

# Copy project files
COPY . .

# Create directory for cloned repos during audit
RUN mkdir -p /tmp/gemini-mythos-audit && chmod 777 /tmp/gemini-mythos-audit

# Make start script executable
RUN chmod +x /app/start.sh

# Expose ports for Streamlit (8501) and Lobster Trap Proxy (8080)
EXPOSE 8501
EXPOSE 8080

# Run the start script
CMD ["/app/start.sh"]
