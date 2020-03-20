import sqlite3

database = './test-db.db'

# #this line creates the file 'database = './file-name.db' - if it doesn't exist, if it does exist, it connects
# connection = sqlite3.connect(database)
# #cursor lets you execute sql commands
# cursor = connection.cursor()


def insert_song_into_songs(title, artist, duration, release_year):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    likes = 0 #set likes to 
    with connection:
        cursor.execute("INSERT INTO songs (title, artist, duration, release_year, likes) VALUES (?, ?, ?, ?, ?)", (title, artist, duration, release_year, likes))


def select_songs(select_by = '*', search_by = ''):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        cursor.execute(f"SELECT {select_by} FROM songs {search_by}")
        return cursor.fetchall()

#insert_song_into_songs("Pick Me Up", "Perfume", 4, 2014)
#insert_song_into_songs("Future Pop", "Perfume", 4, 2018)
print(select_songs())