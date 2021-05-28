import flask as flask
from models import *

app = flask.Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


@app.route("/", methods=["GET"])
def main_page():
    movies = list(Movie.select().dicts())
    return flask.render_template("movies.pug", movies=movies)


@app.route("/database/movies", methods=["GET"])
def get_movie_database():
    movies = list(Movie.select().dicts())
    return flask.render_template("movies.pug", movies=movies)


@app.route("/database/directors", methods=["GET"])
def get_directors_database():
    directors = list(Director.select().dicts())
    return flask.render_template("directors.pug", directors=directors)


@app.route("/database/actors", methods=["GET"])
def get_actors_database():
    actors = list(Actor.select().dicts())
    return flask.render_template("actors.pug", actors=actors)


@app.route("/database/queries", methods=["GET"])
def queries():
    return flask.render_template("queries.pug")


if __name__ == "__main__":
    app.run()
