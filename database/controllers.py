from peewee import *
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
    def get_actors_for_movie():
        data = Movie.select(Movie, Actor).join(Actor).where(Movie.movie_id == Actor.movie_id)
        return list(groupby(data.dicts(), lambda x: x["full_name"]))


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

    @staticmethod
    def get_directors_with_movies():
        return list(Director.
                    select(Director, Movie).
                    join(Movie).
                    where(Director.movie_id == Movie.movie_id).
                    dicts())
