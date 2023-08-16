# Використовуємо офіційний базовий образ Python
FROM python:3.9

# Встановлюємо залежності
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копіюємо проєкт у контейнер
COPY . /app/

# Виконуємо міграції
RUN python manage.py migrate

# Відкриваємо порт 8000 для доступу
EXPOSE 8000

# Запускаємо сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

