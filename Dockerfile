FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install --with-deps

# Copy source code
COPY . .

# Run scraper + start API
CMD ["bash", "-c", "python main.py && uvicorn api.main:app --host 0.0.0.0 --port 8000"]
