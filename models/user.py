from app import db


class User(db.Model):
    #id (int), username (text), password (text)
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
