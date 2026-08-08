# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Built on [django-fundamentals](https://github.com/thespacedoctor/django-fundamentals) —
update it with `pip install -U django-fundamentals` to pull in shared
auth/permissions/frontend improvements.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
npm install
npm run build:css
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Deploy

See `deploy/deploy-{{ cookiecutter.project_slug }}/` for the Ansible
playbook (Apache + mod_wsgi-express + MariaDB on Ubuntu 24.04 /
DigitalOcean).
