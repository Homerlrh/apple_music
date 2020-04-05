from .. import db
from .playlist_songs import Playlist_Songs
from .user_playlist import user_playlist
from datetime import datetime


class Playlist(db.Model):
    __tablename__ = "playlist"
    __id = db.Column(db.Integer, primary_key=True)
    cover_img = db.Column(db.String(
        999), default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Vinyl_record.svg/1200px-Vinyl_record.svg.png", unique=False, nullable=True)
    name = db.Column(db.String(80), default="unknown",
                     unique=False, nullable=True)
    access = db.Column(db.Boolean, default=True, nullable=False)
    create_user = db.Column(db.String(80), default="unknown",
                            unique=False, nullable=True)
    create_user_id = db.Column(db.Integer(), db.ForeignKey('user._user__id'))
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    # mayebe other users can like other user playlists
    # like = db.Column(db.Integer, default=0, unique=False, nullable=True)
    # song can have many albums and albums can have many songs
    Song_List = db.relationship(
        "Song", secondary=Playlist_Songs, backref=db.backref("Song_List", lazy='dynamic'))
    user_list = db.relationship(
        "user", secondary=user_playlist, backref=db.backref("user_list", lazy='dynamic'))
    # def __repr__(self):
    #     return '<Album {}>'.format(f"Album id: {self.id} Album name: {self.name}")
