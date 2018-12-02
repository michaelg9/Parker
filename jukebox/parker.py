import pprint

from jukebox import Jukebox

player = Jukebox()
player.play()
print(player.get_song_uri('Dancing', 'abba'))
# print(player.get_user())
# player.clear()
