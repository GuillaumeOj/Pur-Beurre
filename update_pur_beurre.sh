#!/usr/bin/bash

repo_dir=$(dirname $(realpath $0))
cd $repo_dir

echo "$(date): $(python manage.py init_db)"
echo "$(date): end of update"
