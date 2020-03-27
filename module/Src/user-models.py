from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate -- pip install flask-migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-alchemy-test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#from app import db

# db.Model - db.Column types:
# Integer() - INT
# String() - ASCII strings - VARCHAR
# Unicode() - Unicode string - VARCHAR or NVARCHAR depending on database
# Boolean() - BOOLEAN, INT, TINYINT depending on db support for boolean type
# DateTime() - DATETIME or TIMESTAMP returns Python datetime() objects.
# Float() - floating point values
# Numeric() - precision numbers using Python Decimal()

#all user model classes inherit from db.Model which is a base class for Alchemy
class User(db.Model):
    id              = db.Column(db.Integer(), primary_key=True)
    email           = db.Column(db.String(120), index=True, unique=True)
    password_hash   = db.Column(db.String(128))
    name            = db.Column(db.String(128))
    date_of_birth   = db.Column(db.String(12))

    def __repr__(self):
        return '<User {}>'.format(self.email) 

class Song(db.Model):
    id              = db.Column(db.Integer(), primary_key=True)
    title           = db.Column(db.String(128))
    artist          = db.Column(db.String(128))
    genre           = db.Column(db.String(128))
    duration        = db.Column(db.Float())
    release_year    = db.Column(db.String(128))
    likes           = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return '<Song {}>'.format(self.title) 

class Lyrics(db.Model):
    id              = db.Column(db.Integer(), primary_key=True)
    song_id         = db.Column(db.Integer(), db.ForeignKey('song.id'))
    language        = db.Column(db.String(128))

    def __repr__(self):
        return '<Lyric {}>'.format(f"Lyrics id: {self.id} for song_id: {self.song_id}")

class  Playlist(db.Model):
    id              = db.Column(db.Integer(), primary_key=True)
    user_id         = db.Column(db.Integer(), db.ForeignKey('user.id'))
    song_id         = db.Column(db.Integer(), db.ForeignKey('song.id'))

    def __repr__(self):
        return '<Playlist {}>'.format(f"Playlist id: {self.id} for user_id: {self.user_id}")


#test area
#db.create_all()

# user1 = User(email='email1', password_hash='some_hash_key')
# user2 = User(email='email2', password_hash='some_hash_key')
# user3 = User(email='email3', password_hash='some_hash_key')

# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)

# song1 = Song(title='Pick Me Up', artist="Perfume", genre="Electro-Pop")
# song2 = Song(title='Future Pop', artist="Perfume", genre="Electro-Pop")
# song3 = Song(title='Tokyo Girl', artist="Perfume", genre="Electro-Pop")

# db.session.add(song1)
# db.session.add(song2)
# db.session.add(song3)

# db.session.commit()

users = User.query.all()
for u in users:
    print(u.email)

songs = Song.query.all()
for s in songs:
    print(s.title)

#playlist1 = Playlist(user_id="1", song_id)