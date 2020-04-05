from .. import db
from sqlalchemy import DateTime
import datetime


class user(db.Model):
    __tablename__   = "user"
    __id            = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(999), unique=False, nullable=True)
    email           = db.Column(db.String(999), unique=True, nullable=False)
    password        = db.Column(db.String(99999), unique=False, nullable=False)
    favorite_song   = db.Column(db.PickleType,
                              default=[], unique=False, nullable=True)
    created_date    = db.Column(DateTime, default=datetime.datetime.utcnow)

# def __repr__(self):
#         return '<User {}>'.format(self.name) 
