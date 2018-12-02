from http.server import BaseHTTPRequestHandler, HTTPServer
from agent.agent import agent
# from queue_dealer.queue_dealer import queue_dealer
from ast import literal_eval
from io import BytesIO

PORT_NUMBER = 7788
HOST_NAME = 'localhost'

class http_handle(BaseHTTPRequestHandler):

# Format to sent a POST to the server
# Send Song{'action':'submit_song', song': <song_name>, 'artist': <artist_name>}
# upvote {'action':'upvote', 'uri': <uri>}
# downvote {'action':'downvote', 'uri': <uri>}
    def evoke_command(self, command):
        if command['action'] ==  'submit_song':
            agent.send_song(command['song'], command['artist'])
        elif command['action'] == 'upvote':
            agent.upvote(command['uri'])
        elif command['action'] == 'upvote':
            agent.downvote(command['uri'])
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

if __name__ == '__main__':
    server = HTTPServer
    httpd = server((HOST_NAME, PORT_NUMBER), http_handle)
    print('Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))