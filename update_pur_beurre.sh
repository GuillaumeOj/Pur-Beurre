#!/usr/bin/bash

echo "==================================================================="
echo "$(date): Starting update pur-beurre"

echo "$(date): $(poetry shell)"
echo "$(date): $(python manage.py init_db)"
exit

echo "$(date): End of update"
echo "==================================================================="
