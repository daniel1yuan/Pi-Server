#!/bin/sh

#This file is used to deploy this copy of PiServer to production version

#Copy all files from source directory to webapps
cp -r ./PiServer /hdd/webapps/piserver

#Migrate and collect status
python /hdd/webapps/piserver/PiServer/manage.py makemigrations
python /hdd/webapps/piserver/PiServer/manage.py migrate
python /hdd/webapps/piserver/PiServer/manage.py collectstatic

#Restart Server
supervisorctl restart PiServer
