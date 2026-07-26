class Movie:
    def __init__(self, title, director, year, genres=None):
        self.title = title
        self.director = director
        self.year = year
        
        if genres is not None:
            self.genres = genres
        else:
            self.genres = []