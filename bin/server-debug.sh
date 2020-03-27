#!/bin/bash
export FLASK_APP=main.py
export FLASK_ENV=development

py -m flask run --port 4000 --no-reload
