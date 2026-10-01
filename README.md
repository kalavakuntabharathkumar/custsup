# Customer Support Ticketing Platform

A runnable Django REST Framework API and small React admin dashboard starter for tracking support tickets. Uses SQLite by default for a quick demo and can be configured for MySQL. Includes ticket filtering, assignment, status updates, tests, and a GitHub Actions CI workflow.

## Backend
`cd backend && python -m venv .venv` (activate it), `pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py createsuperuser`, `python manage.py runserver`.
API: `http://127.0.0.1:8000/api/tickets/`; admin: `/admin/`.

Set `DB_ENGINE=mysql` and the `MYSQL_*` environment variables to use MySQL. SQLite is the default. The API currently uses Django session/basic development defaults; configure production security and authentication before deployment.

## Frontend
In another terminal: `cd frontend && npm install && npm run dev`. Set `VITE_API_URL` if the API is not at `http://127.0.0.1:8000/api`.

This is a starter project. The example resume metrics (agent counts, ticket-time reduction, code volume) are not measured by this repository and should only be used if independently verified.
