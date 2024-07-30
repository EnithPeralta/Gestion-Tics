#!/bin/bash

# Activar el entorno virtual (si estás usando uno)
source venv/bin/activate
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
