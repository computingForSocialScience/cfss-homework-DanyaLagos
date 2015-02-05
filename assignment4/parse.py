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
    sumLong=0
    sumLat=0
    for row in permits:
        sumLong += float(row[128])
        sumLat += float (row[129])

        avgLong = sumLong/len(permits)
        avgLat = sumLat/len(permits)
    return avgLong, avgLat

print get_avg_latlng()
# CHECKED. CONFIRMED THAT IT WORKS: (41.78634532257143, -87.58974489214286)

permits = readCSV('permits_hydepark.csv')
def zip_code_barchart(x):
    '''Plots and saves a .jpg bar chart of contractor zipcodes.'''    
    
    zipcode_list = []
    for i in range (len(x)):
        zipcode = x[i][28]
        zipcode_list.append(zipcode)

    plt.hist(zipcode_list, bins=10)
    plt.title("Zip Codes")
    img.save("barchart.jpg")

zip_code_barchart(permits)

