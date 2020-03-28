import sqlite3

#this line creates the file demo.db if it doesn't exist, if it does exist, it connects
connection = sqlite3.connect('demo.db') #note that you can create an in memory database for testing with replacing db name with ':memory:'

#cursor lets you execute sql commands
cursor = connection.cursor()

#SQLite only has five data types: NULL, INTEGER, REAL, TEXT, BLOB

# class Songs:
#   self.cover = cover
#         self.__name = name
#         self.__author = author
#         self.__duration = duration
#         self.__lyrics = lyrics
#         self.__year = year
# cursor.execute("""CREATE TABLE songs (
#     name text,
#     author text,
#     duration real,
#     lyrics text,
#     year integer
# )""")

cursor.execute("INSERT INTO songs (title, artist, duration, release_year, likes) VALUES ('dream dream dream', 'madeon', 5.5, 2016, 0)")

cursor.execute("SELECT * FROM songs")

print(cursor.fetchall()) #prints - [('dream dream dream', 'madeon', 5.5, 'lyrics here', 2016)]

# Preventing SQL Injection wtih placeholders
#cursor.execute('INSERT INTO songs VALUES (?, ?, ?, ?, ?)', ('obj.title, obj.artist, obj.duration, obj.lyrics, obj.release_year'))

#Select statements with placeholders
#cursor.execute('SELECT * FROM songs WHERE title=?', ('song title'))

connection.commit()

connection.close()

