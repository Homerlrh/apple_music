import sqlite3
from sqlite3_controller import *
from sql_lite import *

#init_db()

database = './orange-music.db'
connection = sqlite3.connect(database)
cursor = connection.cursor()

insert_user_into_users('justin@admin.com', 'some_password_hash', 'justin', 'someDOB')
insert_user_into_users('homer@admin.com', 'some_password_hash', 'homer', 'someDOB')
insert_user_into_users('gurmeet@admin.com', 'some_password_hash', 'gurmeet', 'someDOB')

insert_artist_into_artists('perfume')

insert_song_into_songs('Let Me Know', 1, 4, 2018)

insert_into_artist_songs(1,1)

insert_like_into_song_user_likes(1, 1)

insert_favorite_into_user_favorite_songs(1, 1)

insert_album_into_albums('single', 'electro-pop', '2017')

insert_into_artist_albums(1, 1)

insert_like_into_album_user_likes(1, 1)

insert_into_album_songs(1, 1)

insert_lyric_into_lyrics(1, 'english', 'let me know lyrics')

insert_playlist_into_playlists(1, 'My Playlist', 1)

insert_into_playlist_songs(1, 1)