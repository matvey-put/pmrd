FROM python:3.11-slim

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Сначала обновляем pip и устанавливаем/обновляем numpy, затем все остальное
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Настройка путей (с учетом твоей структуры папок из прошлого шага)
ENV PYTHONPATH=/app/data-pipeline
WORKDIR /app/data-pipeline

CMD ["python", "main.py"]