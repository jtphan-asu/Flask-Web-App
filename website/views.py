from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

def login():
    return render_template("login.html")

def sign_up():
    return render_template("sign_up.html")
