class Song:
    '''
        Store the songs in a class attribute
    '''
    all_songs = []
    def __init__(self, name):
        self.name = name
        Song.add_songs_to_collection(self)

    @classmethod
    def add_songs_to_collection(cls, song):
        cls.all_songs.append(song)

    @classmethod
    def show_all_songs(cls):
        print([song.name for song in cls.all_songs])

happy = Song("Happy")
uptown_funk = Song("UpTown Funk")

Song.show_all_songs()