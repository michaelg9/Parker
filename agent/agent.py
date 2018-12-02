from song.song import song
from queue_dealer.queue_dealer import queue_dealer

class agent():

    def __init__(self):
        self.queue_dealer = queue_dealer()

    # Method to receive the songs the user wants to be played
    def send_song(self, song_name, song_artist):
        song = song(song_name, song_artist)
        self.queue_dealer.enqueue_song(song)

    # Upvote a song
    def upvote(self, uri):
        self.queue_dealer.vote_song(uri)

    # Downvote a song
    def downvote(self, uri):
        self.queue_dealer.vote_song(uri, -1)
