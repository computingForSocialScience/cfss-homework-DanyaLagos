from bs4 import BeautifulSoup
import sys
import requests
import csv
import json

#TO ACTIVATE THIS FUNCTION:
#UNCOMMENT LINES 26, 53 and make sure that LINES 50, 54 are COMMENTED.
#THEN, ENTER NAME OF ARTIST.

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    name = name.replace('', '%20')
    url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    
    req = requests.get(url)
    assert req.ok, 'No record found.'
    
    dict = req.json()
    assert dict.get('artists').get('items'), 'Artist not found.'
    
    id = dict['artists']['items'][0]['uri']
    id = id.split(':')[2]
    
    #print(id)
    return(id)

#TO ACTIVATE THIS FUNCTION:
#UNCOMMENT LINES 50, 54 and make sure that LINES 26, 53 are UNCOMMENTED.
#THEN, ENTER ARTIST ID. EXAMPLE: 100XHjSImMmzeQFUbKuuFm 


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id
    
    req = requests.get(url)
    assert req.ok, 'No record found.'

    dict = req.json()
    assert dict.get('name'), 'Artist not found.'

    keys = {}
    keys['followers'] = dict['followers']['total']
    keys['genres'] = dict['genres']
    keys['id'] = dict['id']
    keys['name'] = dict['name']
    keys['popularity'] = dict['popularity']
    #print(keys)
    return(keys)

#fetchArtistId(sys.argv[1])
#fetchArtistInfo(sys.argv[1])
