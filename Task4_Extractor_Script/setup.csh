#!/bin/csh
python3 -m venv .
source "$PWD/bin/activate"
pip install -r dependencies.txt
