import sys
import pandas
import networkx
import random
import csv 
import requests
from io import open
from artistNetworks import *
from analyzeNetworks import *
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
	name = fetchArtistInfo(artistId)['name']
	

