# Timer

Requirements: 
- Python 3.6
- Django 1.9

How to install:

1. Delete db.sqlite3 file and migration folders in the app and blog folder
2. Install ckeditor (pip install django-ckeditor)
3. Migrate database
(python manage.py makemigrations app, python manage.py makemigrations blog, python manage.py migrate)
4. Run server (python manage.py runserver)
