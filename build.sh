#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies from production.txt (which includes gunicorn)
pip install -r requirements/production.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate