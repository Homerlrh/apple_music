import importlib


class Database_Controller:
    #create, retrieve, update, delete
    def __init__(self, database_name, create_method, retrieve_method, update_method, delete_method):
        self.__database_name = database_name
        self.__create_method = create_method
        self.__retreive_method = retrieve_method
        self.__update_method = update_method
        self.__delete_method = delete_method

    @property
    def addSong(self):
        return self.__create_method

    @property
    def getSong(self):
        return self.__retreive_method


# db = importlib.import_module('sql-database/sqlite3-controller', package=None)

#sqlite3 = Database_Controller("sqlite3", db.insert_song_into_songs, db.select_songs, "", "")

# database = db.Database()
# mock_database = Database_Controller("mock_database", database.getSongs, database.addSong, "", "")