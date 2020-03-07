import importlib
db = importlib.import_module('database')
db_controller = importlib.import_module('database-controller')

class Platform_Engine:
    def __init__(self, database):
        self.__database = database

    def getSong(self, search_parameter, search_method):
        if search_parameter != "":
            search_method(search_parameter)

    def getAllSongs(self):
        return self.__database.getSong()

    def addSong(self, title, artist, duration, release_year):
        self.__database.addSong(title, artist, duration, release_year)


    
