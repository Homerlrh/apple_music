class artists:
    def __init__(self, name, DOB, year):
        self.name = name
        self.dob = DOB
        self.follower = 0
        self.year = year
        self.album = []

    def artist_info(self):
        return {"name": self.name, "Date of Birth": self.dob, "Follower": self.follower}

    @property
    def album(self):
        return self.album

    @property
    def followers(self):
        return self.follower

    @followers.setter
    def followers(self):
        self.follower += 1

    @album.setter
    def album(self, obj):
        return self.album.append(obj)
