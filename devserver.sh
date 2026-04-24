#!/bin/sh
source .venv/bin/activate
python -u -m flask --app main --debug run -p $PORT