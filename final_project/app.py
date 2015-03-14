from flask import Flask, render_template, request, redirect, url_for
import pymysql

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=25)])
	email TextField('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [
		validators.Required(), 
		validators.EqualTo('confirm', message='Passwords must match')
		])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the Terms of Service.', [validators.Required()])


app = Flask(__name__) #This creates the app object. 

@app.route('/') #Creates the text of a web page. 
def make_index_resp():
	return(render_template('index.html'))

if __name__ == '__main__': #tells the app to start. 
	app.run()