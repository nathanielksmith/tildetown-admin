#!/bin/bash

PORT=8888
INSTALL_ROOT=/town/src/tildetown-admin
APP_ROOT=$INSTALL_ROOT/ttadmin

VENV=/town/venvs/ttadmin

source $VENV/bin/activate
export DJANGO_SETTINGS_MODULE=settings_live
cd $APP_ROOT
gunicorn -b0.0.0.0:$PORT ttadmin.wsgi
