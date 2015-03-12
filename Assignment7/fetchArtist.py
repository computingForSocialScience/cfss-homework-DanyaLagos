from bs4 import BeautifulSoup
import sys
import requests
import csv
import json


def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """

    url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    
    req = requests.get(url)
    
    data = req.json()

    if not req.ok:
        print "error: " + data['error']['message']
        return "error: " +data['error']['message']


     
    if len(data['artists']['items']) > 0:
        return data['artists']['items'][0]['id']
    else:
        return 'error: no artist found'
    

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id
    
    req = requests.get(url)
    assert req.ok, 'No record found.'

    data = req.json()
    assert data.get('name'), 'Artist not found.'

    artist_info = {}
    artist_info['followers'] = data['followers']['total']
    artist_info['genres'] = data['genres']
    artist_info['id'] = data['id']
    artist_info['name'] = data['name']
    artist_info['popularity'] = data['popularity']
    
    return artist_info 

#print fetchArtistId(sys.argv[1])
#print fetchArtistInfo(sys.argv[1])
