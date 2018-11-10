release: python manage.py migrate --no-input
web: uwsgi engine/wsgi/uwsgi.ini
celeryworker: celery worker -A bubbles.celeryconf:app --loglevel=info -E