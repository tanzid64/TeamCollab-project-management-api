# TeamCollab Project Management
A project management api

## Technology
- Framework: Django REST Framework
- Database: SQLite
- JWT Authentication


# API Endpoints
- PostMan Documentation: https://documenter.getpostman.com/view/32603042/2sA3drGu9j


## Deployment

The first thing to do is to clone the repository:

```bash
  git clone https://github.com/tanzid64/TeamCollab-project-management-api.git
  cd TeamCollab-project-management-api/
```
Create a virtual environment to install dependencies in and activate it:
<br/>
For windows:
```bash
  python -m venv .venv
  .venv\Scripts\activate
```
For Ubuntu:
```bash
  virtualenv .venv
  source .venv/bin/activate
```
Then install the dependencies:

```bash
  pip install -r requirements.txt
```

Apply migrations:

```bash
  python manage.py migrate
```
Create an admin account:

```bash
  python manage.py createsuperuser
```
Start the django application::

```bash
  python manage.py runserver
```

That's it! You should now be able to see the demo application.
Browse:
- HomePage:  http://localhost:8000/
- Admin Panel:  http://localhost:8000/admin/
- Swagger Documentation: http://localhost:8000/api/schema/swagger-ui/
- Schema Download: http://localhost:8000/api/schema/



