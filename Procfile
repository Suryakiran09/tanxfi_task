web: powershell -Command "pip install -r requirements.txt ; python manage.py makemigrations ; python manage.py migrate ; python manage.py runserver 127.0.0.1:8000"
redis: redis-server
celery-beat: celery -A tanxfi_task beat -l info
celery-worker: celery -A tanxfi_task worker --pool=solo -l info