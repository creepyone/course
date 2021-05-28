import flask as flask
from models import *

app = flask.Flask(__name__)


@app.route("/database/movies", methods=["GET"])
def get_movie_database():
    return str(list(Movie.select().dicts()))


@app.route("/database/directors", methods=["GET"])
def get_directors_database():
    return str(list(Director.select().dicts()))


@app.route("/database/actors", methods=["GET"])
def get_actors_database():
    return str(list(Actor.select().dicts()))


if __name__ == "__main__":
    app.run()
