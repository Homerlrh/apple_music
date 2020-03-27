from .. import db


class Album(db.Model):
    __tablename__ = "album"
    __id = db.Column(db.Integer, primary_key=True)
    cover_img = db.Column(db.String(
        999), default="https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/512/unknown-icon.png", unique=False, nullable=True)
    name = db.Column(db.String(80), default="unknow",
                     unique=False, nullable=True)
    author = db.Column(db.String(80), default="unknow",
                       unique=False, nullable=True)
    genre = db.Column(db.String(80), default="unknow",
                      unique=False, nullable=True)
    year = db.Column(db.Integer, default=9999, unique=False, nullable=True)
    like = db.Column(db.Integer, default=0, unique=False, nullable=True)
    Song_list = db.relationship("Song", backref="Album")

    # def __repr__(self):
    #     return "sth"
