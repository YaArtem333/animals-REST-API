from flask_sqlalchemy import SQLAlchemy
from my_app import application

db = SQLAlchemy()
db.init_app(application.app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    animal_type = db.Column(db.String, nullable=False, unique=True)
    chipperId = db.Column(db.ForeignKey('account.id'))

class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.ForeignKey('animal.animal_type'))


def create_table():
    with application.app.app_context():
        db.create_all()