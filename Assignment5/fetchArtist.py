from bs4 import BeautifulSoup
import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    name = name.lower().replace('', '%20')
    url ="https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    r = requests.get(url)
    assert r.ok, 'No record found.'
    data = r.json()
    assert data.get('artists').get('items'), 'Artist not found.'
    artist_id = data['artists']['items'][0]['id']
    return artist_id

fetchArtistId('Nickleback')

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    pass 


fetchArtistId(sys.argv[1])
fetchArtistInfo(sys.argv[1]                        )