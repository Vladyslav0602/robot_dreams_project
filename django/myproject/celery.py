import os
import logging
from celery import Celery

# Налаштування для логування Celery в файл
log_file = 'celery.log'
log_level = logging.INFO  # або інший рівень логування

# Налаштування логгера Celery
celery_logger = logging.getLogger('celery')
celery_logger.setLevel(log_level)

# Додаємо обробник для запису логів у файл
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(log_level)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

celery_logger.addHandler(file_handler)

# Налаштування Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# Функція для логування інформації про завдання
@app.task(bind=True)
def debug_task(self):
    print('Завдання виконано: {0!r}'.format(self.request))
