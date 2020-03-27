import os
import pylast
import math


class get_info:

    def __init__(self):
        self.network = pylast.LastFMNetwork(api_key=os.getenv("API_KEY"), api_secret=os.getenv("API_SECRET"),
                                            username=os.getenv("API_usename"), password_hash=pylast.md5(os.getenv("API_passwor")))

    # get song
    def get_cover_art(self, artist, album):
        cover_art = pylast.Album(artist, album, self.network).get_cover_image()
        return cover_art

    def get_style(self, artist, album):
        try:
            Album = pylast.Album(artist, album, self.network)
            Tag = Album.get_top_tags(limit=None)
            return Tag[0].item.name
        except:
            return None

    def get_date(self, artist, album):
        Album = pylast.Album(artist, album, self.network)
        data = Album.get_wiki_published_date()
        return data

    # track
    def get_song_cover(self, artist, album):
        try:
            return pylast.Track(artist, album, self.network).get_cover_image()
        except:
            return None

    def get_Track_date(self, artist, album):
        Track = pylast.Track(artist, album, self.network)
        data = Track.get_wiki_published_date()
        return data

    def get_duration(self, artist, album):
        Track = pylast.Track(artist, album, self.network)
        return millisToMinutesAndSeconds(Track.get_duration().real)


def millisToMinutesAndSeconds(millis):
    minutes = math.floor(millis / 60000)
    seconds = ((millis % 60000) / 1000)
    return f"{minutes}:{seconds}"
