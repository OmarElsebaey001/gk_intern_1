#!/bin/csh
python -m venv .

source "$PWD/venv/bin/activate"

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate


echo "Run `python manage.py runserver` to start the server"
echo "Happy Hacking!"