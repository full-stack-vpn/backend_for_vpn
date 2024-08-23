# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    gnupg \
    libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app/

# Копируем проект и устанавливаем зависимости
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry install --no-root --only main

# Копируем код приложения
COPY . /app/

# Указываем команду по умолчанию
CMD ["poetry", "run", "python", "start.py"]

#миграции откомичивать только если что то надо менять
CMD ["poetry", "run", "alembic", "upgrade", "header"]
