# Використовуємо базовий образ Python
FROM python:3.8

# Встановлюємо залежності та копіюємо файли проєкту
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# Встановлюємо змінні середовища для Flask
ENV FLASK_APP=app2.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=4200

# Запускаємо Flask
CMD ["flask", "run"]
