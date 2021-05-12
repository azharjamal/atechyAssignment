JWTAuthAPI
JWT Authentication for API

Create Working Folder Cd into

Create Virtal Env
virtualenv venv

Activate Virtual
venv\scripts\activate

Get Clone of Repository:
git clone

Install required Packages:
pip install django django-rest-framework django-cors-headers pip install djangorestframework_simplejwt

Make Migration:
python manage.py makemigrations python manage.py migrate

Create Super User:
python manage.py createsuperuser

Login into Admin Panel and Add Role Entries As 'Admin' and 'User'

Run Server:
python manage.py runserver

Create User List from Following url:

http://127.0.0.1:8000/api/appuser/

Sample User Signup Json:
{ "firstname": "david", "lastname": "john", "emailaddress": "david.john@gmail.com", "password": "secret1", "role": 1 }

After User Creation you can Login Same User into App Sign in and return JWT Token

http://127.0.0.1:8000/api/jwtauth/login/

Sample JSON input
{

"emailaddress": "david.john@gmail.com",
"password": "secret1",
"role": 1
}

It will return refresh and access token like: "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDkwMjUxOCwianRpIjoiY2I1NzU1MGI3NTVmNDZlN2ExNTE4NTkzMDU0YTdhYjkiLCJ1c2VyX2lkIjozfQ.AUqYkWf2SPflkOBvetv2svOHhLwG6Vo1PaI3u4E5SeE", "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODE2NDE4LCJqdGkiOiJkYjM2Y2I1ZmEzNDI0ZGE1YjcxMTg1OWM1ZDNiMjA2NSIsInVzZXJfaWQiOjN9.x-ZagsNwtXv1-2xDzpR38vIj3oW2-uDee2bZX5bL3q8"
