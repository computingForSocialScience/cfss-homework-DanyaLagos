import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id + '/albums?market=US&album_type=album'
    req = requests.get(url)
    assert req.ok, 'No record found.'
    data = req.json()
    assert data.get('items'), 'No artist found.'
    albumidlist = []
    for album in data['items']:
    	albumidlist.append(album['id'])

    return albumidlist
    


def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = "https://api.spotify.com/v1/albums/" + album_id

    req = requests.get(url)
    assert req.ok, 'No record found.'

    data = req.json()
    assert data.get('name'), 'No album found.'

    album_info = {}
    album_info['artist_id'] = data['artists'][0]['id']
    album_info['album_id'] = album_id
    album_info['name'] = data['name']
    album_info['year'] = data['release_date'][0:4]
    album_info['popularity'] = data['popularity']
    
    return album_info

#print fetchAlbumIds("2BTZIqw0ntH9MvilQ3ewNY")
#print fetchAlbumInfo('3uedCd4LBx3WwkAU70jPRI')