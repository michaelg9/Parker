from queue_dealer.queue import queue
from jukebox.jukebox import Jukebox as Juke

class queue_dealer():
    # Put songs into the queue if it is not there
    # if it is there just return a message saying that
    def __init__(self):
        self.queue = queue()
        self.jukebox = Juke()

    def enqueue_song(self, song):
        if not queue.is_in_the_queue():
            self.queue.push(song)
        else:
            print('This song is already in the queue')

    # Remove the song from the queue and send it to be played
    def send_song(self):
        song = self.queue.pull()
        if not song == None:
            self.jukebox.append_song(song.song_uri)
        print('No song in the list')

    def vote_song(self, song_uri, vote=1):
        self.queue.vote_song(song_uri, vote)

    def play_next():
        self.send_song()