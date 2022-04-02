from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/movies/<code>", methods=['GET'])
def get_movie(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        response = app.response_class(
            response=dumps(movies.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies", methods=['GET'])
def get_movies():
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        response = app.response_class(
            response=dumps(
                movies.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies", methods=['POST'])
def create():
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies  
    try:
        movies = dbmov.movies
        movies.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies/<code>", methods=['PUT'])
def update(code):
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        movies.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies/<code>", methods=['DELETE'])
def delete(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        movies.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")
