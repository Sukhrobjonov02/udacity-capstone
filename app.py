import os
from flask import Flask, jsonify, abort, request
from models import setup_db
from flask_cors import CORS
from models import Movie, Actor, db
import traceback

def create_app(test_config=None):
    
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': 
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    # GET METHODS

    @app.route('/actors')
    def actors():
        actors = Actor.query.all()
        return jsonify({
                "success": True,
                "result": [actor.about() for actor in actors],
            }), 200
    
    @app.route('/movies')
    def movies():
        movies = Movie.query.all()
        return jsonify(
            {
                "success": True,
                "result": [movie.about() for movie in movies]
            }
        )
    
    # DELETE METHODS
    
    @app.route('/actors/<id>', methods=['DELETE'])
    def delete_actor(id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()
        except Exception:
            abort(400)

        return jsonify({
            "success": True,
            "deleted": id,
        }), 200

    @app.route('/movies/<id>', methods=['DELETE'])
    def delete_movie(id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()
        except Exception:
            abort(400)

        return jsonify({
            "success": True,
            "deleted": id,
        }), 200

    # POST METHODS



    @app.route('/actors', methods=['POST'])
    def add_actor():
        body = request.get_json()
        print(body)

        try:
            actor = Actor()
            actor.id = body['id']
            actor.name = body['name']
            actor.age = body['age']
            actor.gender = body['gender']
            actor.insert()
        except Exception:
            abort(400)
        
        return jsonify({
            'success': True,
            'actor': [actor.about()],
        }), 200

    @app.route('/movies', methods=['POST'])
    def add_movie():
        body = request.get_json()
        print(body)

        try:
            movie = Movie()
            movie.id = body['id']
            movie.title = body['title']
            movie.release_date = body['release_date']
            movie.genres = body['genres']
            movie.insert()
        except Exception:
            abort(400)
        
        return jsonify({
            'success': True,
            'movie': [movie.about()],
        }), 200
    
    # PATCH METHODs

    @app.route('/actors/<id>', methods=['PATCH'])
    def update_actor(id):
        body = request.get_json()

        actor = Actor.query.filter(Actor.id==id).one_or_none()

        if not actor:
            abort(400)
        
        try:
            actor_name = body['name']
            actor_age = body['age']
            actor_gender = body['gender']

            if actor_name:
                actor.name = actor_name
            if actor_age:
                actor.age = actor_age
            if actor_gender:
                actor.gender = actor_gender
            
            actor.update()
        except Exception:
            abort(400)
        
        return jsonify({
            'success': True,
            'drinks': [actor.about()],
        }), 200
    
    @app.route('/movies/<id>', methods=['PATCH'])
    def update_movie(id):
        body = request.get_json()

        movie = Movie.query.filter(Movie.id==id).one_or_none()

        if not movie:
            abort(400)

        try:
            movie_title = body['title']
            movie_release_date = body['release_date']
            movie_genres = body['genres']

            if movie_title:
                movie.title = movie_title
            if movie_release_date:
                movie.release_date = movie_release_date
            if movie_genres:
                movie.genres = movie_genres
            
            movie.update()
        except Exception as e:
            traceback.print_exc(e)  # Print the exception details for debugging
            abort(400)
        
        return jsonify({
            'success': True,
            'drinks': [movie.about()],
        }), 200
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
