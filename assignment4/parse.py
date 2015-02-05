import csv
import sys

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
    hppermits = readCSV('permits_hydepark.csv')
    SumLong=0
    SumLat=0
    for row in hppermits:
        SumLong += float(row[127])
        SumLat += float (row[128])

        avgLong = sumLong/len(permits)
        avgLat = sumLat/len(permits)
    return avgLong, avgLat
get_avg_latlng()

def zip_code_barchart(x):
    zipcode_list = []
    for i in range (len(x)):
        zipcode = x[i][28]
        zipcode_list.append(zipcode)

    plt.hist(zipcode_list, bins=10)
    plt.title("Zip Codes")
    img.save("barchart.jpg")

zip_code_barchart(permits)
