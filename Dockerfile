FROM python:3.10-slim

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 fonts-liberation libnss3 libatk-bridge2.0-0 libxss1 libgtk-3-0 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2 libxshmfence1 libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

ENV DISPLAY=:99

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add script
COPY script.py .

CMD ["python", "script.py"]
