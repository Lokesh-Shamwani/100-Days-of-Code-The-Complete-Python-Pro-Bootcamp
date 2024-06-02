from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

# Authorization url
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
# Token url
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

SPOTIFY_SEARCH_ENDPOINT = f"https://api.spotify.com/v1/search/{os.getenv('API_TOKEN')}"

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# -------------------------------------------------------------------------------------------
# --> STEP 01
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
year = date.split("-")[0]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# -------------------------------------------------------------------------------------------
# --> STEP 02
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR USERNAME GOES HERE",
    )
)
user_id = sp.current_user()["id"]
# -------------------------------------------------------------------------------------------
# --> STEP 03
song_uris = []
for song in song_names:
    result = sp.search(q=f"track: {song}, year: {year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# -------------------------------------------------------------------------------------------
# --> STEP 04
# create a new private playlist with the name "YYYY-MM-DD Billboard 100",

my_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description="Take Top 100 music from date in past",
)
my_playlist_id = my_playlist["id"]
response_add_tracks = sp.user_playlist_add_tracks(
    user=user_id, playlist_id=my_playlist_id, tracks=song_uris
)
