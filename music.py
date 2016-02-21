import sys
import spotipy
import spotipy.util as util
from random import randint

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()


token = util.prompt_for_user_token(username,scope,client_id='205af94aa7d34bd3b9bf45e8067e0e05',client_secret='3ffea37fdd9b449daecc87d6bbb3bca5',redirect_uri='https://example.com/callback')

if token:
        #print "fuck"
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(20,120)
    sad = [""]
    for item in results['items']:
        track = item['track']
        sad += str(track['preview_url'])
        print str(track['preview_url']) + " " + track['name']
    #print randomEntry(sad)
else:
    print "Can't get token for", username
