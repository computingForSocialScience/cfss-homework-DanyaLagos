from bs4 import BeautifulSoup
import sys
import requests
import csv
import json


def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    name = name.replace('', '%20')
    url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    
    req = requests.get(url)
    assert req.ok, 'No record found.'
    
    data = req.json()
    assert data.get('artists').get('items'), 'No artist found.'
    
    id = data['artists']['items'][0]['uri']
    id = id.split(':')[2]
    
    return(id)


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

    keys = {}
    keys['followers'] = data['followers']['total']
    keys['genres'] = data['genres']
    keys['id'] = data['id']
    keys['name'] = data['name']
    keys['popularity'] = data['popularity']
    
    return(keys)

#print fetchArtistId(sys.argv[1])
#print fetchArtistInfo(sys.argv[1])
