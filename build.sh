#!/bin/bash
# Activar el entorno virtual (si estás usando uno)
source venv/Scripts/activate
set -o errexit
pip install -r requirements.txt
python ./ProjectService/manage.py collectstatic --no-input
python ./ProjectService/manage.py migrate