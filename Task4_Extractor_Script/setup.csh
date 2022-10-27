#!/bin/csh
python3 -m venv v0

source "$PWD/v0/bin/activate"

pip3 install -r requirements.txt

echo "Extraction Starting..."

python3 "app/index.py"

echo "Extraction Completed!"

echo "You will find the results in : $PWD/result.csv"