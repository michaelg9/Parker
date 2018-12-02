from queue_dealer.queue import queue

class queue_dealer():
    # Put songs into the queue if it is not there
    # if it is there just return a message saying that
    def __init__(self):
        self.queue = queue()

    def enqueue_song(self, song):
        if not queue.is_in_the_queue():
            self.queue.push(song)
        else:
            print('This song is already in the queue')

    # Remove the song from the queue and send it to be played
    def send_song(self):
        song = self.queue.pull()
        if not song == None:
            pass
        #michaels
        pass

    def vote_song(self, song_uri, vote=1):
        self.queue.vote_song(song_uri, vote)
