import flask as flask
from models import *

app = flask.Flask("__main__")


@app.route("/database/movies", methods=["GET"])
def get_movie_database():
    return list(Movie.select().dicts()), 200


@app.route("/database/directors", methods=["GET"])
def get_directors_database():
    return list(Director.select().dicts())


@app.route("/database/actors", methods=["GET"])
def get_actors_database():
    return list(Actor.select().dicts())


if __name__ == "__main__":
    app.run()
