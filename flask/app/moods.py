import spotipy
import random
from routes import *

sad_uri = 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V'
happy_uri = 'spotify:artist:7MhMgCo0Bl0Kukl93PZbYS'

spotify = spotipy.Spotify()
sad_results = spotify.artist_top_tracks(sad_uri)
happy_results = spotify.artist_top_tracks(happy_uri)

sad = []
happy = []

for track in sad_results['tracks'][:10]:
	sad.append(str(track['preview_url']))

for track in happy_results['tracks'][:10]:
	happy.append(str(track['preview_url']))

if(res <= 0):
	print(random.choice(sad))
else:
	print(random.choice(happy))
