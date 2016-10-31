#!/bin/sh

#This file is used to deploy this copy of PiServer to production version

#Copy all files from source directory to webapps
cp -r /home/pi/Documents/Projects/PiServer/PiServer /webapps/PiServer

#Migrate and collect status
python /webapps/PiServer/PiServer/manage.py migrate
python /webapps/PiServer/PiServer/manage.py collectstatic

#Restart Server
supervisorctl restart PiServer
