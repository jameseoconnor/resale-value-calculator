#!/bin/bash

# Activate virtualenv 
source venv/bin/activate

# get the latest code 
git pull

# Get the env vars 
set -o allexport
source .env
set +o allexport


function setup_development_environment() {
    export ENV="DEV"
    export DJANGO_SETTINGS_MODULE=website.dev_settings
    cd website/
    python3 manage.py runserver
}

function setup_production_environment() {
    export ENV="PROD"
    export DJANGO_SETTINGS_MODULE=website.prod_settings
    cd website/
    nohup gunicorn --workers=$GUN_WORKERS_PROD website.wsgi -b $APP_HOST_PROD:$APP_PORT_PROD
}

PS3="Choose an Environment: " 
options=("Development" "Production")
select menu in "${options[@]}";

do
  echo -e "\nSetting up $menu ($REPLY) environment"
  if [[ $menu == "Production" ]]; then
    setup_production_environment;
  else
    setup_development_environment;
  fi
done
