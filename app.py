import os
from flask import Flask, jsonify, abort, request
from models import setup_db
from flask_cors import CORS
from models import Movie, Actor, db
import traceback

from auth import AuthError, requires_auth

def create_app(test_config=None):
    
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE')
        return response

    @app.route('/')
    def greeting():
        return jsonify({"greet": "Hello, I am FSND Grad"})

    # GET METHODS

    @app.route('/actors')
    @requires_auth('get:actors')
    def actors(payload):
        actors = Actor.query.all()

        return jsonify({
                "success": True,
                "result": [actor.about() for actor in actors],
            }), 200
    
    @app.route('/movies')
    @requires_auth('get:movies')
    def movies(payload):
        movies = Movie.query.all()

        return jsonify(
            {
                "success": True,
                "result": [movie.about() for movie in movies]
            }
        )
    
    # DELETE METHODS
    
    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()
        except Exception:
            abort(422)

        return jsonify({
            "success": True,
            "deleted": id,
        }), 200

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()
        except Exception:
            abort(422)

        return jsonify({
            "success": True,
            "deleted": id,
        }), 200

    # POST METHODS

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        body = request.get_json()

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        try:
            actor = Actor(
                name=name,
                age=age,
                gender=gender
            )
            actor.insert()

        except Exception:
            abort(422)
        
        return jsonify({
            'success': True,
            'posted': [actor.about()],
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        body = request.get_json()

        try:
            movie = Movie()
            movie.title = body['id']
            movie.title = body['title']
            movie.release_date = body['release_date']
            movie.genres = body['genres']
            movie.insert()

        except Exception:
            abort(422)
        
        return jsonify({
            'success': True,
            'posted': [movie.about()],
        }), 200
    
    # PATCH METHODs

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, id):
        body = request.get_json()

        actor = Actor.query.filter(Actor.id==id).one_or_none()

        if not actor:
            abort(404)
        
        try:
            actor_age = body['age']
            if actor_age:
                actor.age = actor_age
            
            actor.update()

        except Exception:
            abort(422)
        
        return jsonify({
            'success': True,
            'updated': [actor.about()],
        }), 200
    
    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, id):
        body = request.get_json()

        movie = Movie.query.filter(Movie.id==id).one_or_none()

        if not movie:
            abort(404)

        try:
            if 'title' in body:
                movie.title = body.get('title')
            if 'release_date' in body:
                movie.release_date = body.get('release_date')
            if 'genres' in body:
                movie.genres = body.get('genres')
            
            movie.update()

        except Exception:
            abort(422)
        
        return jsonify({
            'success': True,
            'updated': [movie.about()],
        }), 200
    
    @app.errorhandler(400)
    def invalid_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Invalid Request"
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401
    
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403
    
    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Content"
        }), 422
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
                "success": False,
                "error": 500,
                "message": "Internal Server Error"
            }), 500
    
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code


    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
