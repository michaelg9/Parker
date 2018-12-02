import spotipy
import spotipy.util as util

class Jukebox:
#pip3 install git+https://github.com/plamere/spotipy.git --upgrade
    CLIENT_ID='0709595414ba4972898d1750c24387f2'
    CLIENT_SECRET='86a399c8acb8442a89cef5b47a4ae4f5'
    REDIRECT_URI='https://example.com/callback/'

    def __init__(self):
        username = '12165139391'
        token = util.prompt_for_user_token(self.CLIENT_ID, scope='playlist-modify-public user-modify-playback-state', client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI)
        if not token:
            print("Can't get token for", username)
            sys.exit()

        self.__sp = spotipy.Spotify(auth=token)
        self.__sp.trace = False
        self.__user = self.__sp.me()
        self.__playlist = self.__sp.user_playlist_create(self.__user['id'], 'demo', public=True, description='Jukebox')
        self.__current_song = None

    def play(self, song_id='7clUVcSOtkNWa58Gw5RfD4'):
        self.append_song(song_id)
        self.append_song('4wtR6HB3XekEengMX17cpc')
        # uncomment with premium
        self.__sp.start_playback(device_id=None, context_uri=self.__playlist['uri'], uris=None, offset = None)

    def clear(self):
        self.__sp.user_playlist_unfollow(self.__user['id'], self.__playlist['id'])

    def __delete_song(self, song_id):
        self.__sp.user_playlist_remove_all_occurrences_of_tracks(self.__user['id'], self.__playlist['id'], [song_id], snapshot_id=None)

    def append_song(self, song_id):
        # assert self.__get_playlist_size() == 2

        self.__sp.user_playlist_add_tracks(self.__user['id'], self.__playlist['id'], [song_id], position=None)
        # assert self.__get_playlist_size() == 1

    def __refresh_playlist(self):
        self.__playlist = self.__sp.user_playlist(self.__user['id'], playlist_id=self.__playlist['id'], fields=None)

    def get_playlist_size(self):
        self.__refresh_playlist()
        return self.__playlist['tracks']['total']

    def get_currently_played(self):
        return self.__sp.current_user_playing_track()

    def get_user(self):
        return self.__user
    
    def get_song_uri(self, name, artist, limit=1):
        return self.__sp.search(q='track:{} artist:{}'.format(name, artist), limit=limit)['tracks']['items'][0]['uri']

    def next_song_exists(self):
        self.__refresh_playlist()
        return self.__playlist['tracks']['next']