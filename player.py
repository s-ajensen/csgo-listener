import spotipy
from spotipy.oauth2 import SpotifyOAuth

# client_id =
# client_secret =
redirect_url = "http://localhost:8888/callback"
scope = "user-modify-playback-state user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri=redirect_url, scope=scope))

def play():
    if not sp.currently_playing()["is_playing"]:
        sp.start_playback()


def pause():
    if sp.currently_playing()["is_playing"]:
        sp.pause_playback()
