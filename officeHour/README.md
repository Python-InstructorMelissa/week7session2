# Django project

## Create Environment:
This should NEVER be created in the same folder that the project will be in.  This will always remain local to your machine

------------------------------------------------------------------
 Mac/Linux: | python3 -m venv djangoPy3Env 
------------------------------------------------------------------
 Windows (command prompt): | python -m venv djangoPy3Env
------------------------------------------------------------------

## Activate Environment:

------------------------------------------------------------------
 Mac/Linux: | source djangoPy3Env/bin/activate                         
------------------------------------------------------------------
 Windows (command prompt): | call djangoPy3Env\Scripts\activate       
------------------------------------------------------------------
 Windows (git bash) : | source djangoPy3Env/Scripts/activate         
------------------------------------------------------------------


## Install packages:
- pip install django bcrypt

other pip packages you might use:
ipython - better shell view
Pillow - helps with upload
gunicorn - deployment
django-environ - hide secret key

## Create Project:
1. Navigate to where the project folder will be
2. Make sure the environment is active

- django-admin startproject projectName .
- python manage.py startapp appName

## Spin 'er up
Now test that so far everything is working

- python manage.py runserver

click link in terminal or navigate to 127.0.0.1:8000 (localhost:8000)
As long as you see the space shuttle you are good to go

## Edit project and create models
Most of the work will be done in the folder created with the startapp command but there are a few little changes you will need to make and some you will want to make in the 1st folder.  


## After models creation
after you have created your models you are ready to create the database

- python manage.py makemigrations
- python manage.py migrate

## Create Django Admin user

- python manage.py createsuperuser

follow prompts

## Test database in shell
You can add data to the database before any other things are done right after creating the database

- python manage.py shell

### Once that shell is running:
- from appName.models import *

from here you can run several CRUD commands

## Finish Edits
Once the database is created and you have something to display created you can spin up your app again and work with it running.