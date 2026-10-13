# EduFlow Django Full-Stack Project

This project is a complete Django + HTML + CSS + JavaScript student registry application inspired by the uploaded reference video.

## Features

- Regular user registration
- Login / logout
- User-specific student records
- Dashboard statistics
- Student directory
- Search by name, email or mobile
- Course filtering
- Add student
- Edit student
- Delete student
- JavaScript delete confirmation
- Responsive sidebar
- Pagination
- SQLite database
- Django admin

## Windows setup

Open this folder in VS Code.

```bash
python -m venv env
```

PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

CMD:

```cmd
env\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Optional admin:

```bash
python manage.py createsuperuser
```

Run:

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

For a regular user, open:

http://127.0.0.1:8000/register/

Frontend:
- HTML -> templates/core/
- CSS -> static/css/style.css
- JavaScript -> static/js/script.js

Backend:
- Models -> core/models.py
- Forms -> core/forms.py
- Views -> core/views.py
- URLs -> core/urls.py

The base template attaches the frontend assets:

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/script.js' %}"></script>
```
