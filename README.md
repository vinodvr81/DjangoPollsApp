# DjangoPollsApp
From Django documentation polls app practice

[1]. django-admin startproject <Project Name>

ex: django-admin startproject <mysite

[2]. python manage.py runserver

[3]. To start a app

python manage.py startapp <app name>

ex: python manage.py startapp polls

for any db tables that needs to be added

[4]. python manage.py makemigrations <app name>

ex: python manage.py makemigrations polls

[5]. To run migrate so as to create those model tables in your database: below is the command

python manage.py migrate

[6]. To check for any problems in the project

ex: python manage.py check;

[7]. To play around with the free API, Django gives shell. To start shell we need to use below command:

ex: python manage.py shell

[8]  To create a user who can login to the admin site.

ex: python manage.py createsuperuser