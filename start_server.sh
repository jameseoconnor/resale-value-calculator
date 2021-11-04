#!/bin/sh

# Activate virtualenv 
source venv/bin/activate

# get the latest code 
git pull

function setup_development_environment() {
    export ENV="DEV"
    export DJANGO_SETTINGS_MODULE=website.dev_settings
    python3 website/manage.py runserver
}

function setup_production_environment() {
    export ENV="PROD"
    export DJANGO_SETTINGS_MODULE=website.prod_settings
    python3 website/manage.py runserver 0.0.0.0:8000
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
