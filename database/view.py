import flask as flask
from models import *
import controllers
from pprint import pprint

app = flask.Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


@app.route("/", methods=["GET"])
def main_page():
    movies = list(Movie.select().dicts())
    return flask.render_template("movies.pug", movies=movies)


@app.route("/database/movies", methods=["GET"])
def get_movie_database():
    movies = controllers.MovieController.get_all_movies()
    return flask.render_template("movies.pug", movies=movies)


@app.route("/database/directors", methods=["GET"])
def get_directors_database():
    movies, lengths = controllers.MovieController.get_movies_directors()
    pprint(movies)
    pprint(lengths)
    return flask.render_template("directors.pug", movies=movies, lengths=lengths)


@app.route("/database/actors", methods=["GET"])
def get_actors_database():
    movies, lengths = controllers.MovieController.get_movies_actors()
    return flask.render_template("actors.pug", movies=movies, lengths=lengths)


@app.route("/database/queries", methods=["GET"])
def queries():
    return flask.render_template("queries.pug")


if __name__ == "__main__":
    app.run()
