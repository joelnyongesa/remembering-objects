class Album:
    # Class attribute to keep track of the count of the albums
    album_count = 0
    # vlass constant
    GENRES = ["Hip-Hop", "Pop", "Jazz", "RnB"]

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

joel = Album("Reggae", 2010)
print(Album.album_count)