from jukebox.jukebox import Jukebox

class song():
    # The constructor is responsible to get the uri
    def __init__(self, song_name, song_artist):
        self.song_name = ''
        self.song_artist = ''
        self.uri = ''
        self.votes = 0
        pass # This will come from michaels

    def __hash__(self):
        return self.uri

    def __eq__(self, other):
        return self.uri == other.uri

    def vote(self, vote):
        self.votes += vote