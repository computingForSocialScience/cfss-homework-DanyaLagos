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

print readEdgeList('filename.csv')

'''Function II.2 - '''

def degree(edgeList, in_or_out):
	EdgeList = readEdgeList(EdgeList)