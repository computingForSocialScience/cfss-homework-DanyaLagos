'''Function I.1:
This function takes an artist ID as its only argument 
and returns a list of related artists IDs.'''
def getRelatedartists(artistID):


'''Function I.2:
This function takes two arguments, an artist ID and an integer depth, 
and returns a list of tuples representing the (directed) pairs of 
related artists. 
Make sure your list of edges only lists each edge once, with no duplicates.'''

def getDepthEdges(artistID, depth):


'''Function I.3:
This function takes the exact same arguments as getDepthEdges(), 
but returns the result as a Pandas DataFrame with one row for each edge. 
If getDepthEdges() returns a list of 305 tuples, getEdgeList() should return 
a data frame with 305 rows and two columns. 
This should be a simple function that just calls getDepthEdges() 
and then loads the results into a data frame.'''
def getEdgeList(artistID, depth):


'''Function 1.4: This function takes three arguments: 
an artist ID, a depth value, and a filename for output. 
This function should generate an edge list based on the parameters 
artistId and depth, and write that to a CSV file specified by the 
filename parameter. '''
def writeEdgeList(artistID, depth, filename):
