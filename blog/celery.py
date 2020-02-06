from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
app = Celery()

class Config:
    enable_utc = True
    timezone = 'Europe/Moscow'

app.config_from_object(Config)

app.autodiscover_tasks()