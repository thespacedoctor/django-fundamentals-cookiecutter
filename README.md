# django-fundamentals-cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template that
generates a thin Django project wired to
[django-fundamentals](https://github.com/thespacedoctor/django-fundamentals).

Run this **once** per new web app. Everything reusable (auth, permissions,
base templates, frontend baseline) lives in the `django-fundamentals`
package and is updated afterwards with `pip install -U django-fundamentals`
— this template is not re-run to pick up later changes.

## Usage

```bash
pip install cookiecutter
cookiecutter gh:thespacedoctor/django-fundamentals-cookiecutter
```

You'll be prompted for a project name, author, GitHub org, database backend
(SQLite dev / MariaDB prod, or SQLite-only), and deploy hostname.

## What you get

```
my_project/
├── manage.py
├── pyproject.toml              # pins django-fundamentals, django, gunicorn
├── my_project/
│   ├── settings.py              # merges in django_fundamentals.settings
│   ├── urls.py                  # includes django_fundamentals.urls
│   ├── wsgi.py, asgi.py
├── apps/                        # your project-specific Django apps go here
├── templates/, static/          # project-level overrides layered on django_fundamentals
├── tailwind.config.js, package.json
├── deploy/deploy_<slug>/        # ansible playbook: Apache + mod_wsgi-express + MariaDB
└── .github/workflows/
```

## After generating

```bash
cd my_project
python -m venv .venv && source .venv/bin/activate
pip install -e .
npm install && npm run build:css
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

See `django-fundamentals`'s own docs for the auth/permissions/template
override API this project depends on.
