#!/bin/bash

# Check if scraper is running
FILE=./scrapers/.scraper_pid
if test -f "$FILE"; then
    echo "$FILE exists."
    exit 1
fi

# Create a temp PID file 
echo "scraper is running" > scrapers/.scraper_pid

# Activate virtualenv 
source venv/bin/activate

# get the latest code 
git pull

# Get the env vars 
set -o allexport
source .env
set +o allexport

run_date_friendly=$(date)
run_date=$(date +%s)

function start_scraper() {
  cd scrapers/
  python3 pm_scraper.py 
  rm -rf .scraper_pid
  echo "scraper completed at $run_date_friendly" > log/"$run_date".txt
}

PS3="Choose an Environment: " 
options=("Development" "Production")
select menu in "${options[@]}";

do
  echo -e "\nSetting up $menu ($REPLY) environment"
  if [[ $menu == "Production" ]]; then
    export ENV="PROD";
  else
    export ENV="DEV";
  fi
done

start_scraper

