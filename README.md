# Django Movie API (Django + DRF)

A small, practice Movie API built with Django and Django REST Framework.  
This project was created while learning how to build REST APIs with Django. It helped me understand serializers, views, routing, and basic API workflows.

Why this project
- Simple, focused practice for learning Django REST Framework.
- Useful to understand how models → serializers → views → URLs work together.
- A friendly starting point for a junior developer learning to build and test APIs.

What I learned
- Creating serializers to control JSON output.
- Building API views (function-based or class-based) and using routers.
- Basic authentication and protected endpoints (if enabled).
- Using Postman / curl to interact with endpoints.

Features
- List movies, retrieve details, create/update/delete (depending on project permissions).
- Basic pagination and filtering examples (if implemented).
- Starter authentication examples (token or session-based if configured).

Quick start (Windows)
1. Create and activate a virtual environment
   - python -m venv venv
   - venv\Scripts\activate
2. Install dependencies
   - pip install -r requirements.txt
3. Apply migrations and create a superuser
   - python manage.py migrate
   - python manage.py createsuperuser
4. Run the development server
   - python manage.py runserver

Basic usage examples

- List movies (GET)
  curl:
  ```
  curl http://127.0.0.1:8000/api/movies/list/
  ```

- Get movie detail (GET)
  ```
  curl http://127.0.0.1:8000/api/movies/list/1/
  ```

Project tips for beginners
- Open the browsable API (DRF) in a browser at the endpoints to explore responses visually.
- Use breakpoints or logging to trace how a request flows through serializer -> view -> queryset.
- Try adding a new field to the Movie model, then update the serializer and run migrations to see full-stack changes.
- Read the official DRF tutorial for deeper understanding: https://www.django-rest-framework.org/tutorial/quickstart/

Project structure (example)
- manage.py
- requirements.txt
- app/ (your Django apps, e.g., movies, accounts)
- api/ (routers, views, serializers)

Contributing
- Small fixes and improvements welcome. Create issues or PRs with clear descriptions.

License
- This is a learning project. Add a license file if you want to share it publicly.

Happy coding — a simple project like this is a great way to get comfortable with APIs and Django REST Framework.
