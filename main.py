from flask import Flask, request
import os
from helper import *
import db

app = Flask(__name__)


@app.route('/names', methods = ['GET'])
def names():
    query = '''
    SELECT COUNT(*) FROM (SELECT FirstName FROM Customers GROUP BY FirstName)
    '''
    result = db.run_query(query)
    if result:
        return str(result[0][0])
    else:
        ''

@app.route('/tracks', methods = ['GET'])
def tracks():
    query = '''
    SELECT COUNT(*) FROM Tracks
    '''
    result = db.run_query(query)
    if result:
        return str(result[0][0])
    else:
        ''

@app.route('/tracks-sec', methods = ['GET'])
def tracks_sec():
    query = '''
    SELECT Name, Milliseconds/1000 FROM Tracks
    '''
    return str(db.run_query(query))

@app.route('/customers/', methods = ['GET'])
def customers():
    query = '''
    SELECT * FROM customers  
    '''
    filter = request.args.get('filter')
    if filter:
        query += db.generate_where(filter)
    order = request.args.get('ordering')
    if order:
        query += db.ordering(order)
    query += ';'
    print(query)
    return str(db.run_query(query))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
