


class Database:
    def __init__(self):
        self.__songs = []

    def getSongs(self):
        cache = []
        for song in self.__songs:
            cache.append(f"{song.title}")
        return 
        
    def addSong(self, song):
        self.__songs.append(song)