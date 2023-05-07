from flask import Blueprint, render_template
#current_user object can access login information from user
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

def login():
    return render_template("login.html")

def sign_up():
    return render_template("sign_up.html")
