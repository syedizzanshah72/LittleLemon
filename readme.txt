Little Lemon Restaurant API

API Endpoints:

/api/menu/ - GET all dishes, POST new dish
/api/bookings/ - GET all bookings, POST new booking
/api/registration/ - POST to register user
/api/login/ - POST to login user

Setup:

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

Test with Insomnia:
http://localhost:8000/api/

Database: SQLite
Framework: Django REST Framework