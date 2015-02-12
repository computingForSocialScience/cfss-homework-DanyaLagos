from io import open
import csv 

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """

    f = open('artists.csv', 'w', encoding='utf-8')
    try:
        f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
        for keys in artist_info_list:
            artist_id = keys['id']
            artist_name = keys['name']
            artist_followers = keys['followers']
            artist_popularity = keys['popularity']
            f.write(u'%s,"%s",%d,%d\n' % (artist_id, artist_name, artist_followers, artist_popularity))
    finally:
        f.close()
      
def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """

    f = open('albums.csv,' 'w', encoding='utf-8')
    try:
        f.write(u'ARTIST_ID, ALBUM_ID,ALBUM_NAME,ALBUM_POPULARITY\n')
        for keys in album_info_list:
            artist_id = keys['artist_id']
            album_id = keys['album_id']
            name = keys['name']
            year = keys['year']
            popularity = keys['popularity']
