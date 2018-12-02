import pprint

from jukebox import Jukebox

# export SPOTIPY_CLIENT_ID='0709595414ba4972898d1750c24387f2'
# export SPOTIPY_CLIENT_SECRET='b918d42a7676425e91d573b80edc4d68'
# export SPOTIPY_REDIRECT_URI='https://example.com/callback/'
#python3 parker.py 0709595414ba4972898d1750c24387f2

player = Jukebox()
player.play()
# print(player.get_user())
player.clear()
