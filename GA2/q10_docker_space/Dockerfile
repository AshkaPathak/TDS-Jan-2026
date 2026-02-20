FROM python:3.11-slim

# Create user with UID 1000
RUN useradd -m -u 1000 user

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_PORT=7382
EXPOSE 7382

USER user

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7382"]

