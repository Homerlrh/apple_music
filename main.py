
import importlib
db_controller = importlib.import_module('database-controller')
db = importlib.import_module('database')
app = importlib.import_module('platform-engine')


database = db.Database()
mock_database = db_controller.Database_Controller("mock_database", database.addSong, database.getSongs, "", "")
music_platform = app.Platform_Engine()

music_platform.addSong(mock_database, "some song")

#print(mock_database.__dict__)
print(database.__dict__)
