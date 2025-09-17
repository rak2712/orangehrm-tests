FROM python:3.11-slim

WORKDIR /app

# Install required system dependencies (but NOT Chrome or ChromeDriver)
RUN apt-get update && apt-get install -y \
    unzip curl \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 libxss1 libxcomposite1 libxcursor1 libxdamage1 \
    libxrandr2 xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command to run tests
CMD ["pytest", "tests"]
