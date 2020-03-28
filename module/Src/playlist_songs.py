from .. import db


class Playlist_Songs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    playlist_id = db.Column(
        db.Integer(), db.ForeignKey('playlist._Playlist__.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song._Song__id')
