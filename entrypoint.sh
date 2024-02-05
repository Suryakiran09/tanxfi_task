#!/bin/bash
redis-server &
python manage.py runserver 0.0.0.0:8000 & celery -A tanxfi_task worker -l info & celery -A tanxfi_task beat -l info 