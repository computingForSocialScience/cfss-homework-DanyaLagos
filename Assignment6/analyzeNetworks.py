import requests
import pandas 
import csv 
import networkx
import numpy

"""Function II.1 - takes one argument (a filename) and reads an edge list from a CSV 
with that filename, using the read_csv() function of Pandas. 
It should return a Pandas DataFrame with one row for each edge. 
The function should also make sure that the CSV it reads contains only two columns. 
If it contains more than two columns, print a warning and return a data frame that contains 
only the first two columns."""

def readEdgeList(filename): 
	EdgeList = pandas.read_csv(filename)
	if len(EdgeList.columns) > 2:
		print Warning('WARNING: CSV CONTAINS MORE THAN TWO COLUMNS!')
		first2columns = pandas.read_csv(filename, usecols=[0,1])
		return pandas.DataFrame(first2columns)
	else:
		return pandas.DataFrame(EdgeList)

#print readEdgeList('filename.csv')

'''Function II.2 - uses the value_counts() method of Pandas data frame columns 
to return the in-degree or out-degree (as specified by the second argument in_or_out) 
for all nodes in a given edge list.'''

def degree(EdgeList, in_or_out):
	if in_or_out == 'out':
		return EdgeList['artist1'].value_counts()
	elif in_or_out == 'in':
		return EdgeList['artist2'].value_counts()

#print degree(readEdgeList('filename.csv'), 'in')

'''Function II.3 - takes two data frames as arguments and combines them into one long edge list'''

def combineEdgeLists(edgeList1, edgeList2): 
	initialEdgeList = pandas.concat([edgelist1, edgelist2])
	finalEdgeList = initialEdgeList.drop_duplicates()
	return finalEdgeList

'''Function II.4 - reates a NetworkX Digraph (directed graph) 
from of an edge list in a pandas data frame.'''

def pandasToNetworkX(EdgeList):
	starterlist = EdgeList.to_records(index=False)
	digraph = networkx.DiGraph()
	for artist1,artist2 in starterlist:
		digraph.add_edge(artist1,artist2)
	return digraph 

#pandasToNetworkX(readEdgeList('filename.csv'))

'''Function II.5 - picks a random node from a related-artists network 
that is biased toward picking more central nodes over those on the network's periphery. '''

def randomCentralNote(inputDiGraph):

	dictionary = networkx.eigenvector_centrality(inputDiGraph)
	for key in dictionary:
		newdictionary[key] = dictionary[key]/float(sum(dictionary.values()))
		node = numpy.random.choice(newdictionary.keys(), p=newdictionary.values())
	return node
