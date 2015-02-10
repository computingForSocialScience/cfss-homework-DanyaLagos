import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id + '/albums?market=US&album_type=album'

    req = requests.get(url)
    assert req.ok, 'No record found.'

    dict = req.json()
    assert dict.get('name'), 'Album not found.'

    keys = {}
    keys['followers'] = dict['followers']['total']
    keys['genres'] = dict['genres']
    keys['id'] = dict['id']
    keys['name'] = dict['name']
    keys['popularity'] = dict['popularity']
    
    print(keys)
    return(keys)

def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    pass

fetchAlbumIds('2BTZIqw0ntH9MvilQ3ewNY')