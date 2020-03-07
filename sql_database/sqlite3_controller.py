import sqlite3

# database = './test-db.db'

# #this line creates the file demo.db if it doesn't exist, if it does exist, it connects
# connection = sqlite3.connect(database)
# #cursor lets you execute sql commands
# cursor = connection.cursor()


def insert_song_into_songs(title, artist, duration, release_year):
    database = './test-db.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    #set likes to 
    likes = 0
    with connection:
        cursor.execute("INSERT INTO songs (title, artist, duration, release_year, likes) VALUES (?, ?, ?, ?, ?)", (title, artist, duration, release_year, likes))


def select_songs(search_with = None):
    database = './test-db.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    if not search_with:
        with connection:
            cursor.execute("SELECT * FROM songs")
            return cursor.fetchall()
    else:
        #call the search function
        pass

# insert_song_into_songs("Let Me Know", "Perfume", 4.5, 2017)
# print(select_songs())