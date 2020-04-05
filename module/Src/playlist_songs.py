from .. import db


Playlist_Songs = db.Table("play_songs", db.Column("playlist_id",
                                                  db.Integer, db.ForeignKey('playlist._Playlist__id')),
                          db.Column("song_id", db.Integer,
                                    db.ForeignKey('song._Song__id'))
                          )
