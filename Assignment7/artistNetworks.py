import requests
import pandas 
import csv
'''Function I.1:
This function takes an artist ID as its only argument 
and returns a list of related artists IDs.'''
def getRelatedArtists(artistID):
	url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
	req = requests.get(url)
	assert req.ok, 'No record found.'
	data = req.json()
	assert data.get('artists'), 'No artist found.'

	relatedartist_List = [] 
	for relatedartist in data['artists']:
		relatedartist_List.append(relatedartist['id'])

	return relatedartist_List

#print getRelatedartists("0OdUWJ0sBjDrqHygGUXeCF")


'''Function I.2:
This function takes two arguments, an artist ID and an integer depth, 
and returns a list of tuples representing the (directed) pairs of 
related artists. 
Make sure your list of edges only lists each edge once, with no duplicates.'''

def getDepthEdges(artistID, depth):

	directedPairs = [] # This is the list where the other two lists should be combined.
	directedPairs_checked = [] #Then they should go to this one after they are checked.
	relatedArtists = []
	relatedArtists.append(artistID)

	for i in range(depth):
		for relatedartist in relatedArtists:
			newartists = getRelatedArtists(relatedartist)
			for newartist in newartists:
				directedPairs.append((relatedartist, newartist))
		relatedArtists = newartists
	for tple in directedPairs: 
		if tple not in directedPairs_checked:
			directedPairs_checked.append(tple)

	return directedPairs_checked

#print getDepthEdges("0OdUWJ0sBjDrqHygGUXeCF", 2)

'''Function I.3:
This function takes the exact same arguments as getDepthEdges(), 
but returns the result as a Pandas DataFrame with one row for each edge. 
If getDepthEdges() returns a list of 305 tuples, getEdgeList() should return 
a data frame with 305 rows and two columns. 
This should be a simple function that just calls getDepthEdges() 
and then loads the results into a data frame.'''
def getEdgeList(artistID, depth):
	EdgeList = getDepthEdges(artistID, depth)
	return pandas.DataFrame(EdgeList)

#print getEdgeList("0OdUWJ0sBjDrqHygGUXeCF", 2)

'''Function 1.4: This function takes three arguments: 
an artist ID, a depth value, and a filename for output. 
This function should generate an edge list based on the parameters 
artistId and depth, and write that to a CSV file specified by the 
filename parameter. '''
def writeEdgeList(artistID, depth, filename):
	EdgeList = getEdgeList(artistID, depth)
	EdgeList.to_csv(filename, index=False)

writeEdgeList ("0OdUWJ0sBjDrqHygGUXeCF", 2, "filename.csv")