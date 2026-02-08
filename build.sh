#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements/production.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser (only if doesn't exist)
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='${ADMIN_EMAIL}').exists():
    User.objects.create_superuser(
        email='${ADMIN_EMAIL}',
        password='${ADMIN_PASSWORD}',
        first_name='${ADMIN_FIRST_NAME}',
        last_name='${ADMIN_LAST_NAME}',
        id_no=int('${ADMIN_ID_NO}'),
        security_question='maiden_name',
        security_answer='${ADMIN_SECURITY_ANSWER}'
    )
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF