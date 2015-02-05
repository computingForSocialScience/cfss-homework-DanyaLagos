import csv
import sys
import subprocess 
import pandas
import matplotlib as plt
from collections import Counter
import numpy as np


def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

### enter your code below
def get_avg_latlng():
    '''Computes the average latitude and longitude of construction permits in HP,
    prints it to the console'''
    permits = readCSV('permits_hydepark.csv')
    sumLng=0
    sumLat=0
    for row in permits:
        sumLng += float(row[128])
        sumLat += float (row[129])

        avgLng = sumLng/len(permits)
        avgLat = sumLat/len(permits)
    return avgLng, avgLat

# CHECKED. CONFIRMED THAT IT WORKS: (41.78634532257143, -87.58974489214286)
permits = readCSV('permits_hydepark.csv')

def zip_code_barchart(x):
    '''Plots and saves a .jpg bar chart of contractor zipcodes.''' 
    n = len(readCSV("permits_hydepark.csv"))
    k = readCSV('permits_hydepark.csv')   
    zip_code = []
    z = [28,35,42,49,56,63,70,77,84]
    for i in k: 
        for p in z: 
            if i[p] != "":
                zip_code.append(int(i[p][:5]))

    #print zip_code #<---- works until here. 11:50PM
    zipcode_counts = Counter(zip_code)

    plt.bar(range(len(zipcode_counts)), zipcode_counts.values(), align='center')
    plt.xticks(range(len(zipcode_counts)), zipcode_counts.keys())
    plt.yticks(range(0,6))
    plt.title("Zip Code Frequency")
    plt.grid(True)
    plt.draw()
    plt.savefig("barchart.jpg")
    subprocess.call("open barchart.jpg", shell=True)
    plt.show()

if len(sys.argv) == 1: 
    print get_avg_latlng(permits)
    zip_code_barchart(permits)
if sys.argv[1] == "latlong":
    print get_avg_latlng()
elif sys.argv[1] == "hist":
    zip_code_barchart(permits)
