from flask import Flask, render_template, request, redirect, url_for
import pymysql

import sys
import io
import random
import networkx
import pandas

from artistNetworks import * 
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *

dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
cursor = db.cursor()

app = Flask(__name__)

## THIS IS THE FIRST FUNCTION OF THE ASSIGNMENT
def createNewPlaylist(artistname):

    cursor.execute ('''CREATE TABLE IF NOT EXISTS playlists (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        rootAritst VARCHAR(500) CHARACTER SET utf8
        );
    ''')
    cursor.execute = ('''CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        playlistId INTEGER, 
        songOrder INTEGER, 
        artistName VARCHAR(500) CHARACTER SET utf8,
        albumName VARCHAR(500) CHARACTER SET utf8,
        trackName VARCHAR(500) CHARACTER SET utf8
        );
    ''')
    cursor.execute ('''INSERT INTO playlists (rootArtist) VALUES (%s);   
    ''')

    artistID = fetchArtistId(artistname)
    edge_list = getEdgeList (artist_id, 2)
    digraph = pandasToNetworkX(EdgeList)

    random_artists = []
    for i in range(30): 
        random_artist = randomCentralNote(digraph)
        random_artists.append(random_artist)

    artist_names = []
    album_list = []
    for artist_id in random_artists:
        artist = fetchArtistInfo(artist_id)
        artist_name = artist['name']
        artist_names.append(artist_name)
        album_id_list_ = fetchAlbumIds(artist_id)

        if album_id_list == []:
            print "Error: Empty Spotify 'none type' album id for" artist_name, ". Pass and continue."
            continue 


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))



if __name__ == '__main__':
    app.debug=True
    app.run()