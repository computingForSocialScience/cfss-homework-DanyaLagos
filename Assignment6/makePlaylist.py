import sys
import pandas
import networkx
import random
import csv 
import requests
from io import open
from artistNetworks import *
from analyzeNetworks import *
sys.path.append('../Assignment5/')
from fetchArtist import *
from fetchAlbums import *

if __name__ == '__main__':
	artists = sys.argv[1:]

artistids = []
for name in artists:
	artistID = fetchArtistID(name)
	artistids.append(artistID)

edgelists = []
for i in range(len(artistids)):
	edgelist = getEdgeList(artistids[i], 2)
	edgelists.append(edgelist)

mergedlists = edgelists[0]
for i in range (len(edgelists)):
	mergedlists = combineEdgeLists(mergedlists, edgelists[i])
mergedlists.columns = ['artist1', 'artist2']

g = pandasToNetworkX(medgedlists)

sample30 = []
for i in range(30):
	sample30.append(randomCentralNote(g))

nameslist = []
albumlist = []

for artistID in sample30:
	name = fetchArtistInfo(artistID)['name']
	nameslist.append(name)
	albumids = fetchAlbumIDs(artistID)
	randomalbum = (random.choice(albumids))

randomtracks = []
for album in albumlist:
	url = "https://api.spotify.com/v1/albums/" + album[1] + "/tracks"
	req = requests.get(url)
	data = req.json().get('items')
	randomlist = []
	for i in range(len(data)):
		tracknamestring =  data[i]['name']
		randomlist.append(tracknamestring)
		getrandomtrack = (random.choice(randomlist))
	randomtracks.append(getrandomtrack)

print randomtracks 

f = open('playlist.csv', 'w')
f.write(u'artistname, album name, track name\n')
for i in range(len(randomtracks)):
	artistname = nameslist[i]
	albumname = albumlist[i][0]
	trackname = randomtracks[i]
	f.write(('"' + artistName + '"' + ',' + '"' + albumName + '"' + ',' + '"' + trackName + '"' + '\n'))
f.close()
