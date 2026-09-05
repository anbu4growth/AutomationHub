FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium

RUN playwright install-deps chromium

COPY . .

CMD ["python", "main.py"]