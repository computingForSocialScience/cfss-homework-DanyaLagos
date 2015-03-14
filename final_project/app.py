from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__) #This creates the app object. 

@app.route('/') #Creates the text of a web page. 
def make_index_resp():
	return(render_template('index.html'))

if __name__ == '__main__': #tells the app to start. 
	app.run()