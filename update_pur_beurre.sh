#!/usr/bin/bash

echo "==================================================================="
echo "$(date): Starting update pur-beurre"

echo "$(date): $(poetry shell)"
echo "$(date): $(python manage.py init_db)"
echo "$(date): $(deactivate)"

echo "$(date): End of update"
echo "==================================================================="
