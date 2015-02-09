import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    name = name().replace('', '%20')
    url ="https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    req = requests.get(url)
    print(req)
    print(type(req))


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    pass

fetchArtistId(sys.argv[1])