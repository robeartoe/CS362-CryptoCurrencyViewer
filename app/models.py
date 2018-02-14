# TODO: Implement user model:

from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    currencies = db.relationship('UserCurrencies', backref='author',lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)
#this creates a one-to-many relationship between the user and its currencies
class UserCurrencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Currency {}>'.format(self.currency)
