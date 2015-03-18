from flask import Flask, render_template, request, redirect, url_for
import pymysql


dbname="groceries"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
cursor = db.cursor()

app = Flask(__name__)

class Store(db.Model):
	__tablename__='stores'
	storeName = db.Column(db.String(255))
	zipCode = db.Column(db.String(5))
	communityName = db.Column(db.String(255))
	latitude = db.Column(db.Integer)
	longitude = db.Column(db.Integer)
	


if __name__ == '__main__':
    app.debug=True
    app.run()