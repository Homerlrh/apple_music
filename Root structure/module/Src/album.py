from .. import db


class Album(db.Model):
    __tablename__ = "album"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), default="unknow",
                     unique=True, nullable=True)
    author = db.Column(db.String(80), default="unknow",
                       unique=False, nullable=True)
    genre = db.Column(db.String(80), default="unknow",
                      unique=False, nullable=True)
    year = db.Column(db.Integer, default=9999, unique=False, nullable=True)
    like = db.Column(db.Integer, default=0, unique=False, nullable=True)

    # def __repr__(self):
    #     return "sth"
