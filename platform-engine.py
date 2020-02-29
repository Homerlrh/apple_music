import importlib
db = importlib.import_module('database')
db_controller = importlib.import_module('database-controller')

class Platform_Engine:
    def __init__(self):
        pass

    def getSong(self, database, search_parameter, search_method):
        if search_parameter != "":
            search_method(search_parameter)

    def addSong(self, database, song):
        if song is not None:
            database.addSong(song)


    
