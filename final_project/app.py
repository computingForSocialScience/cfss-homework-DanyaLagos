from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql
from flask.ext.sqlalchemy import SQLAlchemy


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


@app.route('/grocerystores/', methods=['GET'])
def grocerystores():
	if request.method == 'GET':
		results = Store.query.limit(10).offset(0).all()

		json_results = []
		for results in results:
			d = {'STORE NAME'}

if __name__ == '__main__':
    app.debug=True
    app.run()