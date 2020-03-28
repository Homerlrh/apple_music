from .. import db


class Album_Songs(db.Model):
    __tablename__ = "album_songs"
    __id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album._Album__id')
    song_id=db.Column(db.Integer, db.ForeignKey('song._Song__id')
