import pprint

from jukebox import Jukebox

player = Jukebox()
player.play()
print(player.get_song_uri('mamma mia'))
# print(player.get_user())
# player.clear()
