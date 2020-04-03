from .. import db
from .playlist_songs import Playlist_Songs


class Playlist(db.Model):
    __tablename__ = "playlist"
    __id = db.Column(db.Integer, primary_key=True)
    cover_img = db.Column(db.String(
        999), default="https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/512/unknown-icon.png", unique=False, nullable=True)
    name = db.Column(db.String(80), default="unknown",
                     unique=False, nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user._User__.id'))
    # mayebe other users can like other user playlists
    #like = db.Column(db.Integer, default=0, unique=False, nullable=True)
    # song can have many albums and albums can have many songs
    Song_list = db.relationship(
        "Song", secondary=Playlist_Songs, backref=db.backref("song_list", lazy='dynamic'))

    # def __repr__(self):
    #     return '<Album {}>'.format(f"Album id: {self.id} Album name: {self.name}")
