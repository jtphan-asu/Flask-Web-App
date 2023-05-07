from flask import Blueprint, render_template, request, flash
#current_user object can access login information from user
from flask_login import login_required, current_user

from .models import Note
from . import db
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            #Add note then add to db
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

def login():
    return render_template("login.html")

def sign_up():
    return render_template("sign_up.html")
