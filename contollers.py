from peewee import *
from models import Actor, Movie, Director


class MovieController:
    @staticmethod
    def create_movie(title, year, genre, rating, votes) -> None:
        """Создание записи с фильмом"""
        Movie.get_or_create(title=title,
                            year=year,
                            genre=genre,
                            rating=rating,
                            votes=votes)


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
