import copy
from song.song import song
class queue():
    def __init__(self):
        self.queue = set()

    def push(self, song):
        self.queue.add(song)

    def pull(self, song):
        try:
            song = self.queue.pop()
            self.queue.add(song)
            cur = copy.deepcopy(song)
            for elem in self.queue:
                if song.votes < elem.votes:
                    cur = elem
            return self.queue.remove(song)
        except:
            print('cannot pull from the queue')
            return

    def is_in_the_queue(self, song):
        for elem in self.queue:
            if elem.uri == song.uri:
                return True
        return False

    def vote_song(self, song_uri, vote):
        for elem in self.queue:
            if elem.uri == song_uri:
                elem.votes += vote
