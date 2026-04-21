# Stage 1: Build stage
FROM python:3.13-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

# Copy requirements and install to a local directory
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.13-slim

# Add curl here so the healthcheck works!
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Create a non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy only the installed packages and code from the builder
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

# Set environment paths and switch to non-root user
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

# Define how to check if the API is running correctly
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/docs || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]