from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
app = Celery('blog')

app.config_from_object('django.conf:settings', namespace = 'CELERY')
#load task module
app.autodiscover_tasks()