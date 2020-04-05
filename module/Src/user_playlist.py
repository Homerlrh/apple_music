from .. import db


user_playlist = db.Table("user_playlist",
                         db.Column("user_id", db.Integer,
                                   db.ForeignKey('user._user__id')),
                         db.Column("playlist_id", db.Integer,
                                   db.ForeignKey('playlist._Playlist__id')),
                         )
