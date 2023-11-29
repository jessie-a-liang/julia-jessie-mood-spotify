import spotipy
import json
import webbrowser
import spotipy.util as util

credentials = "spotify_keys.json"
with open(credentials, "r") as keys:
    api_tokens = json.load(keys)

client_id = api_tokens["client_id"]
client_secret = api_tokens["client_secret"]
redirectURI = api_tokens["redirect"]
username = api_tokens["username"]

scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public user-read-recently-played'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirectURI)

sp = spotipy.Spotify(auth=token)

recently_played = sp.current_user_recently_played(limit=1,after=None, before=None)
recently_played

song = recently_played['items']
song

artist_id = [song[0]['track']['artists'][0]['id']]
artist_id

track_id = [song[0]['track']['id']]
track_id

oura = 0.5
tfl = 118
weather = 0.7
news = 0.9

tracks = sp.recommendations(artist_id,track_id, target_danceability=news, target_energy=oura, target_valence=weather, target_tempo=tfl, genres=None, limit=15)
track_list = tracks['tracks']
uri_list = []
for track in track_list:
    uri_list.append(track['uri'])

uri_list

my_playlist = sp.user_playlist_create(user=username, name="today", public=True, description="Songs for today")
a = sp.user_playlist_add_tracks(username, my_playlist['id'], uri_list)
a