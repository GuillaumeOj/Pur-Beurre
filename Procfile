release: python manage.py migrate
release: python manage.py init_db
web: gunicorn config.wsgi --log-file -
