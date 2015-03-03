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
	artistID = fetchArtistId(name)
	artistids.append(artistID)

edgelists = []
for i in range(len(artistids)):
	edgelist = getEdgeList(artistids[i], 2)
	edgelists.append(edgelist)

mergedlists = edgelists[0]
for i in range (len(edgelists)):
	mergedlists = combineEdgeLists(mergedlists, edgelists[i]) 

g = pandasToNetworkX(mergedlists)

sample30 = []
for i in range(30):
	sample30.append(randomCentralNode(g))

nameslist = []
albumlist = []

for artistID in sample30:
	name = fetchArtistInfo(artistID)['name']
	nameslist.append(name)
	albumids = fetchAlbumIds(artistID)
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

f = open('playlist.csv', 'w', encoding='utf-8')
try: 
	f.write(u'artist name, album name, track name\n')
	for i in range(len(randomtracks)):
		artistname = nameslist[i]
		albumname = albumlist[i][0]
		trackname = randomtracks[i]
		f.write(u'"%s","%s","%s"\n' % (artist_name,album_name,track_name))
finally:
	f.close()
