from flask import Flask, render_template, request, redirect, url_for
import pymysql

from wtforms import Form, BooleanField, TextField, PasswordField, validators #used to facilitate registration

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=25)])
	email = TextField('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [
		validators.Required(), 
		validators.EqualTo('confirm', message='Passwords must match')
		])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the Terms of Service.', [validators.Required()])


class LoginForm(Form):
	username = TextField('Username')
	password = PasswordField('Password')
form = LoginForm()


app = Flask(__name__)


@app.route('/') #Creates the text of a web page. 
def make_index_resp():
	return(render_template('index.html'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data,
					form.password.data)
		db_session.add(user)
		flash('Thank you for registering!')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

if __name__ == '__main__': #tells the app to start. 
	app.run()



