from http.server import BaseHTTPRequestHandler, HTTPServer
from agent.agent import agent
from jukebox.jukebox import Jukebox
import threading
# from queue_dealer.queue_dealer import queue_dealer
from ast import literal_eval
from io import BytesIO
import time

PORT_NUMBER = 7788
HOST_NAME = 'localhost'

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class http_handle(BaseHTTPRequestHandler):

# Format to sent a POST to the server
# Send Song{'action':'submit_song', song': <song_name>, 'artist': <artist_name>}
# upvote {'action':'upvote', 'uri': <uri>}
# downvote {'action':'downvote', 'uri': <uri>}
    def __init__(self):
        self.agent = agent()

    def evoke_command(self, command):
        if command['action'] ==  'submit_song':
            self.agent.send_song(command['song'], command['artist'])
        elif command['action'] == 'upvote':
            self.agent.upvote(command['uri'])
        elif command['action'] == 'upvote':
            self.agent.downvote(command['uri'])
        elif command['action'] == 'print':
            self.agent.print_list()
        else:
            pass #return a message


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(literal_eval(body.decode("utf-8")))
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

    @threaded
    def process_treaded(self):
        if not self.jukebox.next_song_exists():
            agent.play_next()
        time.sleep(5)



if __name__ == '__main__':
    server = HTTPServer
    http_handle_ = http_handle()
    httpd = server((HOST_NAME, PORT_NUMBER), http_handle)
    hand = http_handle_.process_treaded()
    print('Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
    hand.join()
