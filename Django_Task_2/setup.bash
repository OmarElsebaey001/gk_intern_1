# !/bin/bash
BLUE='\033[0;94m'
Green='\033[1;32m'
BPurple='\033[1;35m'

python3 -m venv v0

source 'v0/bin/activate'

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

printf "\n${BLUE} Run '${BPurple}python3 manage.py runserver${BLUE}' to start the server.\n\n"

printf "${Green} Happy Hacking!\n"
