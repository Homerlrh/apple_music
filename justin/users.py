class users:
    def __init__(self, name, password, DOB, year):
        self.name = name
        self.secret = password
        self.dob = DOB
        self.year = year
        self.favorite = []

    def get_name(self):
        return self.name

    def get_DOB(self):
        return self.dob

    @property
    def favorite(self):
        return self.favorite

    @favorite.setter
    def favorite(self, song):
        self.favorite.append(song)
        return
