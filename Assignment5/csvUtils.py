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
        for artist_info in artist_info_list:
            artist_id = artist_info['id']
            artist_name = artist_info['name']
            artist_followers = artist_info['followers']
            artist_popularity = artist_info['popularity']
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

    f = open('albums.csv', 'w', encoding='utf-8')
    try:
        f.write(u'ARTIST_ID, ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
        for album_info in album_info_list:
            album_artist_id = album_info['artist_id']
            album_id = album_info['album_id']
            album_name = album_info['name']
            album_year = album_info['year']
            album_popularity = album_info['popularity']
            f.write(u'%s,%s,"%s",%s,%s\n' % (album_artist_id, album_id, album_name, album_year, album_popularity))
    finally:
        f.close()