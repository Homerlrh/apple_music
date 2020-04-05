from .. import db
from datetime import datetime
from .user_playlist import user_playlist


class user(db.Model):
    __tablename__ = "user"
    __id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(999), unique=False, nullable=True)
    email = db.Column(db.String(999), unique=True, nullable=False)
    password = db.Column(db.String(99999), unique=False, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    p_list = db.relationship(
        "Playlist", secondary=user_playlist, backref=db.backref("p_list", lazy='dynamic'))


# def __repr__(self):
#         return '<User {}>'.format(self.name)
