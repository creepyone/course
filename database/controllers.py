from models import Actor, Movie, Director
from itertools import groupby


class MovieController:
    @staticmethod
    def create_movie(title, year, genre, rating, votes) -> None:
        """Создание записи с фильмом"""
        Movie.get_or_create(title=title,
                            year=year,
                            genre=genre,
                            rating=rating,
                            votes=votes)

    @staticmethod
    def get_all_movies():
        return list(Movie.select().dicts())

    @staticmethod
    def get_movies_by_genre(genre: str) -> list:
        return list(Movie.select().where(Movie.genre == genre).dicts())

    @staticmethod
    def get_movies_actors():
        data = Movie.select(Movie, Actor).join(Actor).where(Movie.movie_id == Actor.movie_id).dicts()
        return ({key: list(items) for key, items in groupby(data, lambda x: x["title"])},
                {key: len(list(items)) for key, items in groupby(data, lambda x: x["title"])})

    @staticmethod
    def get_movies_directors():
        data = Movie.select(Movie, Director).join(Director).where(Movie.movie_id == Director.movie_id).dicts()
        return ({key: list(items) for key, items in groupby(data, lambda x: x["title"])},
                {key: len(list(items)) for key, items in groupby(data, lambda x: x["title"])})

    @staticmethod
    def get_movies_votes():
        return list(Movie.select(Movie.title, Movie.votes).dicts())

    @staticmethod
    def get_movies_rating():
        return list(Movie.select(Movie.title, Movie.rating).dicts())

    @staticmethod
    def get_movies_year():
        return list(Movie.select(Movie.title, Movie.year).dicts())


class ActorController:
    @staticmethod
    def create_actor(full_name, movie_id) -> None:
        """Создание записи с актером"""
        Actor.get_or_create(full_name=full_name,
                            movie_id=movie_id)


class DirectorController:
    @staticmethod
    def create_director(full_name, movie_id) -> None:
        """Создание записи с режиссёром"""
        Director.get_or_create(full_name=full_name,
                               movie_id=movie_id)

