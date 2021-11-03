#!/bin/sh

sudo su - 
yum update

# Install and Start PostgreSQL
amazon-linux-extras install postgresql13
yum install -y postgresql-server postgresql-devel
/usr/bin/postgresql-setup –-initdb
systemctl enable postgresql
systemctl start postgresql
systemctl status postgresql

# Login to bash 
su - postgres

# Now connect to psql 
psql

# Configure the database
CREATE DATABASE resale_app;
\c resale_app
CREATE ROLE joconnor WITH PASSWORD 'james_password';
# GRANT ALL PRIVILEGES ON resale_app TO joconnor; -- THis won't exist yet 


# Set up an SSH connection between the instance and github
ssh-keygen -t rsa  -b 4096 -C "jamesedoconnor@gmail.com"
cat .ssh/id_rsa.pub  # Remember the passphrase, you will be asked for it when you pull the code
# Copy the public key and create a github key pair 


# Now let;s get the code
yum install git 
git clone <ssh_repo>


# We now have the DB up and running and we have the code
# Now we need the software to run the code 
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
python website/manage.py migrate  # -- get the ident authentication failure here 

# Next we want to change the pg_hba.conf file to allow all localhosts to talk to each other 
systemctl status postgresql # Show us where the data directory is 

vim /var/lib/pgsql/data/pg_hba.conf # Change all ident to trust 

sudo systemctl restart postgresql.service # restart the service 


# Run the server 
python3 website/manage.py runserver 0.0.0.0:8000

#  Website should be up and running now 






