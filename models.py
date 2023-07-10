from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, ARRAY
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL
import json

database_path = DATABASE_URL
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()

def db_drop_create():
    db.drop_all()
    db.create_all()
    db_insert_records()

def db_insert_records():
    actor = (Actor(
        name = "Abdulaziz",
        age = 21,
        gender = 'Male'
    ))

    movie = (Movie(
        title = 'Catch Me if You Can',
        release_date = '2023-07-11',
        genres = ['Action']
    ))

    actor.inser()
    movie.inser()

    actor_movie = actors_movies.insert().values(
        actor_id = actor.id,
        movie_id = movie.id
    )

    db.session.execute(actor_movie)
    db.session.commit()

actors_movies = db.Table('actor_movies',
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)                         
)


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    movies = db.relationship('Movie', secondary=actors_movies, backref=db.backref('actors', lazy=True))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def about(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime, default=datetime.today(), nullable=False)
    genres = Column(ARRAY(String()), nullable=False)

    def __init__(self, title, release_date, genres):
        self.title = title
        self.release_date = release_date
        self.genres = genres

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def about(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'genres': self.genres,
        }

