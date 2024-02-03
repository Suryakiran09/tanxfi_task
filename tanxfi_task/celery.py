# tanxfi_task/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tanxfi_task.settings')

app = Celery("tanxfi_task")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
