import os
import pylast
import math


class get_info:

    def __init__(self):
        self.network = pylast.LastFMNetwork(api_key=os.getenv("API_KEY"), api_secret=os.getenv("API_SECRET"),
                                            username=os.getenv("API_usename"), password_hash=pylast.md5(os.getenv("API_passwor")))

    # get song
    def get_cover_art(self, artist, album):
        try:
            return pylast.Album(artist, album, self.network).get_cover_image()
        except pylast.WSError:
            return None
        except IndexError:
            return None

    def get_style(self, artist, album):
        try:
            Album = pylast.Album(artist, album, self.network)
            Tag = Album.get_top_tags(limit=None)
            return Tag[0].item.name
        except IndexError:
            return None

    def get_date(self, artist, album):
        Album = pylast.Album(artist, album, self.network)
        data = Album.get_wiki_published_date()
        print("date:  ", data)
        return data

    # track
    def get_song_cover(self, artist, album):
        try:
            is_track = pylast.Track(artist, album, self.network)
            return is_track.get_cover_image()
        except pylast.WSError:
            return None

    def get_Track_date(self, artist, album):
        try:
            Track = pylast.Track(artist, album, self.network)
            data = Track.get_wiki_published_date()
            return data
        except pylast.WSError:
            return None
        except IndexError:
            return None

    def get_duration(self, artist, album):
        try:
            Track = pylast.Track(artist, album, self.network)
            return millisToMinutesAndSeconds(Track.get_duration().real)
        except pylast.WSError:
            return None


def millisToMinutesAndSeconds(millis):
    minutes = math.floor(millis / 60000)
    seconds = ((millis % 60000) / 1000)
    return f"{minutes}:{seconds}"
