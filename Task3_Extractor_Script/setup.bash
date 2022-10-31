#!/bin/bash

BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'
BGreen='\033[1;32m'       # Green
BRed='\033[1;31m'         # Red

python3 -m venv v0

source "$PWD/v0/bin/activate"
pip install --upgrade pip

pip3 install -r requirements.txt

printf "${BRed}Extraction Starting...\n\n${BYellow}"

python3 "app/index.py"

printf "\n${BGreen}Extraction Completed!\n\n"

printf "${BPurple}You will find the results in: ${BYellow} $PWD/result.csv \n"