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
    url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist" #forming a readable URL
    
    req = requests.get(url)
    assert req.ok, 'No record found.'
    
    dict = req.json()
    assert dict.get('artists').get('items'), 'Artist not found.'
    
    id = dict['artists']['items'][0]['uri']
    id = id.split(':')[2]
    
    print(id)
    return(id)



def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    pass 

fetchArtistId('Justin Bieber')