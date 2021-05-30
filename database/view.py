import json

import flask
from models import *
import controllers
from pprint import pprint

app = flask.Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


@app.route("/", methods=["GET"])
def main_page():
    movies = controllers.MovieController.get_all_movies()
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


@app.route("/static", methods=["GET"])
def static_request():
    movies = controllers.MovieController.get_all_movies()
    return flask.render_template("static_query.pug", movies=movies)


@app.route("/static", methods=["POST"])
def static_queries():
    genre = flask.request.form["genre"]
    movies = controllers.MovieController.get_movies_by_genre(genre)
    return flask.render_template("static_query.pug", movies=movies)


@app.route("/dynamic", methods=["GET"])
def dynamic_request():
    movies = controllers.MovieController.get_all_movies()
    return flask.render_template("dynamic_query.pug", movies=movies)


@app.route("/get_genre", methods=["POST"])
def get_genre():
    data = json.loads(flask.request.data)
    print(data)
    genre = data["genre"].strip()
    if genre == "":
        movies = controllers.MovieController.get_all_movies()
    else:
        movies = controllers.MovieController.get_movies_by_genre(genre)
    return flask.jsonify(movies)


if __name__ == "__main__":
    app.run()
