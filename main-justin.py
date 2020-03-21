
from sql_database.sqlite3_controller import *
import sys
import importlib
db_controller = importlib.import_module('database-controller')
#db = importlib.import_module('sql-database/sqlite3-controller', package=None)

sys.path.insert(0, '/sql-database/sqlite3_controller')


app = importlib.import_module('platform-engine')


# initialize sqlite3
sqlite3_database = db_controller.Database_Controller(
    "sqlite3", insert_song_into_songs, select_songs, "", "")
# bind sqlite3_database's create song method to addSong on Platform_Engine
music_platform = app.Platform_Engine(sqlite3_database)

#title, artist, duration, release_year
#music_platform.addSong("Let Me Know", "Perfume", 4.5, 2017)

print(music_platform.getAllSongs())
