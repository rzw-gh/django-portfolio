# Django Project

This is a Django web application built using Python and the Django framework.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Django (latest version or your preferred version)
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup

Follow these steps to set up the project locally.

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/rzw-gh/django-portfolio.git
cd django-portfolio
```

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

Activate On Windows:

```bash
venv\Scripts\activate
```

Activate On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7.Ready to use:
if you didn't get any error. head over to `http://127.0.0.1:8000/` in your browser to view the app.
