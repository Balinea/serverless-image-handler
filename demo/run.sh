#!/bin/bash

echo "virtualenv --no-site-packages env"
virtualenv --no-site-packages env
echo "source env/bin/activate"
source env/bin/activate
echo "python -m pip install pip==9.0.3"
python -m pip install pip==9.0.3
pip install -r requirements.txt

./server.py
