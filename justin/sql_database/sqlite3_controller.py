import sqlite3

database = './orange-music.db'

# #this line creates the file 'database = './file-name.db' - if it doesn't exist, if it does exist, it connects
# connection = sqlite3.connect(database)
# #cursor lets you execute sql commands
# cursor = connection.cursor()

default_album_cover = 'https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/512/unknown-icon.png'



#insert_song_into_songs("Pick Me Up", "Perfume", 4, 2014)
#insert_song_into_songs("Future Pop", "Perfume", 4, 2018)
#print(select_songs())




#users
def select_users(select_by = '*', search_by = ''):
    table = 'users'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_user_into_users(email, password_hash, name, date_of_birth):
    table = 'users'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (email, password_hash, name, date_of_birth) VALUES (?, ?, ?, ?)", (email, password_hash, name, date_of_birth))


#artists
def select_artists(select_by = '*', search_by = ''):
    table = 'artists'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_artist_into_artists(name):
    table = 'artists'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (name) VALUES (?)", (name,))


#artist_songs
def select_artist_songs(select_by = '*', search_by = ''):
    table = 'artist_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_into_artist_songs(artist_id, song_id):
    table = 'artist_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (artist_id, song_id) VALUES (?,?)", (artist_id, song_id))


#songs
def select_songs(select_by = '*', search_by = ''):
    table = 'songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_song_into_songs(title, artist_id, duration, release_year):
    table = 'songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (title, artist_id, duration, release_year) VALUES (?, ?, ?, ?)", (title, artist_id, duration, release_year))


#song_user_likes
def select_song_user_likes(select_by = '*', search_by = ''):
    table = 'song_user_likes'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_like_into_song_user_likes(song_id, user_id):
    table = 'song_user_likes'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (song_id, user_id) VALUES (?,?)", (song_id, user_id))


#user_favorite_songs
def select_user_favorite_songs(select_by = '*', search_by = ''):
    table = 'user_favorite_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_favorite_into_user_favorite_songs(user_id, song_id):
    table = 'user_favorite_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (user_id, song_id) VALUES (?,?)", (user_id, song_id))


#albums
def select_albums(select_by = '*', search_by = ''):
    table = 'albums'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#default album cover used here
def insert_album_into_albums(title, genre, release_year, cover_image = default_album_cover):
    table = 'albums'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (title, genre, release_year, cover_image) VALUES (?, ?, ?, ?)", (title, genre, release_year, cover_image))


#artist_albums
def select_artist_albums(select_by = '*', search_by = ''):
    table = 'artist_albums'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_into_artist_albums(artist_id, album_id):
    table = 'artist_albums'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (artist_id, album_id) VALUES (?, ?)", (artist_id, album_id))


#album_user_likes
def select_album_user_likes(select_by = '*', search_by = ''):
    table = 'album_user_likes'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_like_into_album_user_likes(album_id, user_id):
    table = 'album_user_likes'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (album_id, user_id) VALUES (?, ?)", (album_id, user_id))


#album_songs
def select_users(select_by = '*', search_by = ''):
    table = 'album_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_into_album_songs(album_id, song_id):
    table = 'album_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (album_id, song_id) VALUES (?, ?)", (album_id, song_id))


#lyrics
def select_lyrics(select_by = '*', search_by = ''):
    table = 'lyrics'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_lyric_into_lyrics(song_id, language, lyrics):
    table = 'lyrics'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (song_id, language, lyrics) VALUES (?, ?, ?)", (song_id, language, lyrics))


#playlists
def select_playlists(select_by = '*', search_by = ''):
    table = 'playlists'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()


def insert_playlist_into_playlists(user_id, title, song_id):
    table = 'playlists'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (user_id, title, song_id) VALUES (?, ?, ?)", (user_id, title, song_id))


#playlist_songs
def select_playlist_songs(select_by = '*', search_by = ''):
    table = 'playlist_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()


def insert_into_playlist_songs(playlist_id, song_id):
    table = 'playlist_songs'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (playlist_id, song_id) VALUES (?,?)", (playlist_id, song_id))


