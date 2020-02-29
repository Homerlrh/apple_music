class song:
    def __init__(self, cover, name, author, duration, lyrics, year):
        self.cover = cover
        self.__name = name
        self.__author = author
        self.__duration = duration
        self.__lyrics = lyrics
        self.__year = year
        self.like = 0

    def get_name(self):
        return self.__name

    def get_lyrics(self):
        return self.__lyrics

    def get_author(self):
        return self.__author
