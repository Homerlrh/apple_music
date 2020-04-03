from .. import db


Album_Songs = db.Table("album_songs", db.Column("ablum_id", db.Integer, db.ForeignKey('album._Album__id')),
                       db.Column("song_id", db.Integer,
                                 db.ForeignKey('song._Song__id'))
                       )
