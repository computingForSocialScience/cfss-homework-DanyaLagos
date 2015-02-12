import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    
    artistinfo_list = []
    albuminfo_list = []

    for artist in artist_names:
    	artist_id = fetchArtistId(artist)
    	artist_info = fetchArtistInfo(artist_id)
    	artistinfo_list.append(artist_info)

    	album_id = fetchAlbumIds(artist_id)
    	for albumid in album_id:
    		album_info = fetchAlbuminfo(albumid)
    		albuminfo_list.append(album_info)

    writeArtistsTable(artistinfo_list)
    writeAlbumsTable(albuminfo_list)

    plotBarChart()




