#!/bin/bash 

# ugliest deploy script ever! =P

scp -r ../* suggestmydomain@suggestmydomain.com:/home/suggestmydomain/apps_wsgi/suggestmydomain/
