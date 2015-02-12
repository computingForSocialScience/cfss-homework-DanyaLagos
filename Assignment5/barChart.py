# The two lines below import packages for unicode and matplotlib.
import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData(): #First function to get Bar Chart Data
    f_artists = open('artists.csv') #Opens artists.csv for editing and makes a variable out of it.
    f_albums = open('albums.csv') #Opens albums.csv for editing and makes a variable out of it.

    artists_rows = csv.reader(f_artists) #Creates rows in artists.csv
    albums_rows = csv.reader(f_albums) #Creates rows in albums.csv

    artists_header = artists_rows.next() #Creates header in artists.csv
    albums_header = albums_rows.next() #Creates header in albums.csv

    artist_names = [] # New list in which to store artist names.
    
    decades = range(1900,2020, 10) #For upcoming decade dictionary, sets limits and intervals for how it will store dates by decade.
    decade_dict = {} #Creates decae dictionary.
    for decade in decades: #Sets conditions on what happens to this dictionary.
        decade_dict[decade] = 0 #Sets initial value to 0
    
    for artist_row in artists_rows: #Sets conditions on rows in artists.csv
        if not artist_row: #condition: skip if it does not correspond to a row in artists.csv
            continue
        artist_id,name,followers, popularity = artist_row # set following values to go in entries to rows section of arists.csv
        artist_names.append(name) #puts all artist names in the list

    for album_row  in albums_rows: #sets conditions on rows in albums.csv
        if not album_row: #condition: skip if it does not correspond to a row in albums.csv
            continue
        artist_id, album_id, album_name, year, popularity = album_row #sets following values to go in entries to rows section of albums.csv
        for decade in decades: #conditions on decades it assigns to album
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)): #takes year in album and counts the decade in which the year belongs
                decade_dict[decade] += 1
                break #ends the condition on the album row

    x_values = decades #for upcoming chart, sets decades as the x value
    y_values = [decade_dict[d] for d in decades] #for upcoming chart, sets number of albums as y value
    return x_values, y_values, artist_names #brings all of the values generated in the function for the upcoming barchart function

def plotBarChart(): #this is the beginning of the function that creates the bar chart 
    x_vals, y_vals, artist_names = getBarChartData() #calls up the values generated in the previous function
    
    fig , ax = plt.subplots(1,1) #determines what figure will be used, what the parameters will be 
    ax.bar(x_vals, y_vals, width=10) #tells it to make bar chart with width of 10
    ax.set_xlabel('decades') #assigns label for x values
    ax.set_ylabel('number of albums') #assigns label for y values 
    ax.set_title('Totals for ' + ', '.join(artist_names)) #assigns label for general graph 
    plt.show() #crates the bar chart


    
