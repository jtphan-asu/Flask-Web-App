#import from current package with "."
from . import db

#Helps log users in
from flask_login import UserMixin

#Takes care of date time, timezone
from sqlalchemy.sql import func


#Note Object to store notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    #store id of one of the users. 
    #This is foreign key. Must pass valid user id when we create a note object.
    
    #user.id is referencing User object, and primary key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#User Object
class User(db.Model, UserMixin):
    #Define Schema

    #Unique Primary Key and type of column
    id = db.Column(db.Integer, primary_key=True)

    #Define max length for String
    #Unique means no other user can have same email address
    email = db.Column(db.String(150), unique=True)

    password = db.Column(db.String(150))

    first_name = db.Column(db.String(150))

    #When we create a note, add User Notes class relationship the note id
    notes = db.relationship('Note')