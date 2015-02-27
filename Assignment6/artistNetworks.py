import requests
'''Function I.1:
This function takes an artist ID as its only argument 
and returns a list of related artists IDs.'''
def getRelatedartists(artistID):
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
	url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
	req = requests.get(url)
	assert req.ok, 'No record found.'
	data = req.json()
	assert data.get('artists'), 'No artist found.'

	directedPairs = [] #This is the list where the other two lists should be combined.

	return directedPairs 
	


print getDepthEdges("0OdUWJ0sBjDrqHygGUXeCF", 2)

'''Function I.3:
This function takes the exact same arguments as getDepthEdges(), 
but returns the result as a Pandas DataFrame with one row for each edge. 
If getDepthEdges() returns a list of 305 tuples, getEdgeList() should return 
a data frame with 305 rows and two columns. 
This should be a simple function that just calls getDepthEdges() 
and then loads the results into a data frame.'''
def getEdgeList(artistID, depth):
	pass

'''Function 1.4: This function takes three arguments: 
an artist ID, a depth value, and a filename for output. 
This function should generate an edge list based on the parameters 
artistId and depth, and write that to a CSV file specified by the 
filename parameter. '''
def writeEdgeList(artistID, depth, filename):
	pass 