# Stage 1: Build stage
FROM python:3.13-slim as builder

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.13-slim

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

# Set environment paths and switch to non-root user
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

# Healthcheck for a worker: verify the process is still running
HEALTHCHECK --interval=30s --timeout=3s \
  CMD pgrep -f "python worker.py" || exit 1

CMD ["python", "worker.py"]