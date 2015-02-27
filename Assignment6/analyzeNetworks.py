import requests
import pandas 
import csv 

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

print degree(readEdgeList('filename.csv'), 'in')