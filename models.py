from settings import db
from datetime import datetime

shows_table = Table = db.Table('shows',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False),
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), nullable=False),
    db.Column('start_time', db.DateTime, default=datetime.today(), nullable=False),
    db.PrimaryKeyConstraint('movie_id', 'actor_id', 'start_time')
)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    actors = db.relationship('Actor', secondary=shows_table, backref=db.backref('movies', lazy=True))

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)