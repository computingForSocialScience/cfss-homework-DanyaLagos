import csv
import sys
import matplotlib as plt

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

print get_avg_latlng()
# CHECKED. CONFIRMED THAT IT WORKS: (41.78634532257143, -87.58974489214286)
permits = readCSV('permits_hydepark.csv')

def zip_code_barchart(x):
    '''Plots and saves a .jpg bar chart of contractor zipcodes.''' 
    lines = readCSV('permits_hydepark.csv')   
    zip_code = []
    q = [28,35,42,49,56,63,70,77,84]
    for i in lines: 
        for p in q: 
            if i[p] != "":
                zip_code.append(int(i[p][:5]))

    print zip_code
    plt.hist(zip_code, bins=400)
    plt.title("Zip Codes")
    plt.xlabel("Contractor Zip Codes")
    plt.ylabel("Frequency")
    plt.savefig("barchart.jpg")
    plt.show


if sys.argv[1] == "latlong":
    get_avg_latlng(permits)
elif sys.argv[1] == "hist":
    zip_code_barchart(permits)

