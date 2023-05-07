
*****PROJECT CREATION*****
Create Project Folder

Create website folder that contains static, templates and __init__.py to make a python package.

create main.py auth.py models.py, views.py

run pip install flask

pip install flask-login

pip install flask-sqlalchemy

set up flask application in __init__.py file
link up in main.py file to create_app()

set up views.py
    Blueprint and route
set up auth.py
    login, logoutm signup

create html templates with Jinja
base.html, home.html, login.html, sign_up.html
    base.html contains main template and it extends block title and block content

set up form with POST request for sign_up.html and login.html


put .js file in static if wanting to add own .js

//add to github
git remote add Flask-Web-App https://github.com/jtphan-asu/Flask-Web-App

<script
        type="text/javascript"
        src="{{ url_for('static', filename='index.js') }}"
    ></script>
    
Set up POST, GET requests on auth.py.  Request variable.
    Create input rescritions ( too short password, etc.)
Set up flash messages on base.html

*****SET UP DATABASE*****
Set up sqlite with sqlalchemy

Set up database tables schema under models.py
    User
    Note
Database model is blueprint for how data is stored in database
Utilize sqlalchemy.sql func() to manage date time

Set up foreign key relationships for Note and User
    One User to Many Notes ( One-to-many relationship)


*****CREATE DATABASE*****
add create_database method to __init.py__

//These lines add the user to database session and commit
db.session.add(new_user)
db.session.commit()

*****LOGIN USER*****