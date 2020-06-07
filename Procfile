release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn review.wsgi --log-file -