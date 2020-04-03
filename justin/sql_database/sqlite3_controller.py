import sqlite3

database = './test-db.db'

# #this line creates the file 'database = './file-name.db' - if it doesn't exist, if it does exist, it connects
# connection = sqlite3.connect(database)
# #cursor lets you execute sql commands
# cursor = connection.cursor()

default_album_cover = https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/512/unknown-icon.png

#songs
def select_songs(select_by = '*', search_by = ''):
    table = songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_song_into_songs(title, artist, duration, release_year):
    table = songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"INSERT INTO {table} (title, artist, duration, release_year) VALUES (?, ?, ?, ?)", (title, artist, duration, release_year))

#insert_song_into_songs("Pick Me Up", "Perfume", 4, 2014)
#insert_song_into_songs("Future Pop", "Perfume", 4, 2018)
#print(select_songs())




#users
def select_users(select_by = '*', search_by = ''):
    table = users
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

def insert_user_into_users(email, password_hash, name, date_of_birth):
    table = users
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    likes = 0 #set likes to 
    with connection:
        cursor.execute(f"INSERT INTO {table} (email, password_hash, name, date_of_birth) VALUES (?, ?, ?, ?)", (email, password_hash, name, date_of_birth))


#artists
def select_users(select_by = '*', search_by = ''):
    table = artists
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()





#artist_songs
def select_users(select_by = '*', search_by = ''):
    table = artist_songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()



#songs up there


#song_user_likes
def select_users(select_by = '*', search_by = ''):
    table = song_user_likes
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()


#user_favorite_songs
def select_users(select_by = '*', search_by = ''):
    table = user_favorite_songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#albums
def select_users(select_by = '*', search_by = ''):
    table = albums
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#artist_albums
def select_users(select_by = '*', search_by = ''):
    table = artist_albums
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()


#album_user_likes
def select_users(select_by = '*', search_by = ''):
    table = album_user_likes
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#album_songs
def select_users(select_by = '*', search_by = ''):
    table = album_songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#lyrics
def select_users(select_by = '*', search_by = ''):
    table = lyrics
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()

#playlists
def select_users(select_by = '*', search_by = ''):
    table = playlists
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()


#playlist_songs
def select_users(select_by = '*', search_by = ''):
    table = playlist_songs
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM {table} {search_by}")
        return cursor.fetchall()