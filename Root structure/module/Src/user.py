from .. import db
from sqlalchemy import DateTime
import datetime


class user(db.Model):
    __id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(999), unique=False, nullable=False)
    password = db.Column(db.String(999), unique=False, nullable=False)
    date_of_birth = db.Column(
        db.Date(), default="0000-00-00", unique=False, nullable=True)
    favorite_song = db.Column(db.PickleType,
                              default=[], unique=False, nullable=True)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
