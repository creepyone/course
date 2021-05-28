from peewee import *

db = SqliteDatabase("movies.db")


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    movie_id = IntegerField(primary_key=True)
    title = CharField()
    year = IntegerField()
    genre = CharField()
    rating = FloatField()
    votes = IntegerField()


class Actor(BaseModel):
    actor_id = AutoField(primary_key=True)
    full_name = CharField()
    movie_id = ForeignKeyField(Movie, backref="actors")


class Director(BaseModel):
    director_id = AutoField(primary_key=True)
    full_name = CharField()
    movie_id = ForeignKeyField(Movie, backref="director")


db.create_tables([Movie, Actor, Director], safe=True)