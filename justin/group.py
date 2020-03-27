from artists import artists


class group:
    def __init__(self, group_name, member, year):
        self.name = group_name
        self.num_of_member = member
        self.year = year
        self.follower = 0
        self.album = []
        self.member = []

    def set_member(self):
        for i in range(self.num_of_member):
            artist_name = input("name")
            artist_dob = input("dob")
            year = int(input("year"))
            self.member.append(artists(artist_name, artist_dob, year))

    def get_name(self):
        return self.name

    @property
    def followers(self):
        return self.follower

    @followers.setter
    def followers(self):
        self.follower += 1

    @property
    def album(self):
        return self.album

    @album.setter
    def album(self, obj):
        return self.album.append(obj)
