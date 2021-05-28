import flask as flask
from models import *
import controllers

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
    directors = controllers.DirectorController.get_directors_with_movies()
    return flask.render_template("directors.pug", directors=directors)


@app.route("/database/actors", methods=["GET"])
def get_actors_database():
    actors = controllers.MovieController.get_actors_for_movie()
    return flask.render_template("actors.pug", actors=actors)


@app.route("/database/queries", methods=["GET"])
def queries():
    return flask.render_template("queries.pug")


if __name__ == "__main__":
    app.run()
