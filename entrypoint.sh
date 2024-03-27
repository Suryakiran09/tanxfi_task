#!/bin/bash
redis-server &
python manage.py runserver 0.0.0.0:8000 & celery -A tanxfi_task worker --pool=solo -l info & celery -A tanxfi_task beat -l info 