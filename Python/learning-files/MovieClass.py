class Movie:
    def __init__(self, name, year, director, genres=None):
        self.name = name
        self.year = year
        self.director = director

        if genres is not None:
            self.genres = []
        else:
            self.genres = genres