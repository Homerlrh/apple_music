import os
import pylast
import math
import lyricwikia


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
        except pylast.WSError:
            return None

    def get_date(self, artist, album):
        # try:
        Album = pylast.Album(artist, album, self.network)
        print(Album.__dir__())
        data = Album.get_wiki_published_date()
        print("date:  ", data)
        return data
        # except pylast.WSError:
        #     return None

    # track

    def get_song_cover(self, artist, album):
        try:
            is_track = pylast.Track(artist, album, self.network)
            return is_track.get_cover_image()
        except pylast.WSError:
            return None
        except IndexError:
            return None

    def get_song_date(self, artist, album):
        try:
            Track = pylast.Track(artist, album, self.network)
            data = Track.get_wiki_published_date()
            return data
        except pylast.WSError:
            return None
        except IndexError:
            return None

    def get_duration_2(self, num):
        return sec_to_min(int(num))

    def get_lyrics(self, artist, track):
        try:
            lyrics = lyricwikia.get_lyrics(artist, track)
            return lyrics
        except:
            return None


def sec_to_min(num):
    frac, whole = math.modf(num/60)
    sec = frac*60
    decimal, whoel_num = math.modf(sec)
    if whoel_num/10 <= 1:
        whoel_num = f"0{whoel_num}"
    time = f"{int(whole)}:{whoel_num}"
    return time.split(".")[0]
