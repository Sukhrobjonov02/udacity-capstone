import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS
from models import Movie, Actor

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

    @app.route('/actors')
    def actors():
        actors = Actor.query.all()
        print("ACTORSSSSSSSSSSSSSSSSSSSSSSSSSSSSS", actors)
        data = []
        for actor in actors:
            data.append({
                "id": actor.id,
                "name": actor.name,
                "age": actor.age,
                "gender": actor.gender,
            })
        return jsonify(
            {
                "success": True,
                "result": data
            }
        )
    
    @app.route('/movies')
    def movies():
        movies = Movie.query.all()
        data = []
        for movie in movies:
            data.append({
                "id": movie.id,
                "title": movie.title,
                "release_date": movie.release_date,
                "genres": movie.genres,
            })
        return jsonify(
            {
                "success": True,
                "result": data
            }
        )

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
