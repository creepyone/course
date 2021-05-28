import imdb
import contollers


def get_list_of_movies(quantity: int) -> list:
    """Получить список quantity фильмов, 0 <= quantity <= 250"""
    ia = imdb.IMDb()
    top = ia.get_top250_movies()[:quantity]
    for movie in top:
        yield ia.get_movie(movie.movieID)


def fill_data_base(quantity: int) -> None:
    """Заполнение базы данных"""
    movies = get_list_of_movies(quantity)
    for movie_id, movie in enumerate(movies, start=1):
        controllers.MovieController.create_movie(title=movie["title"],
                                                 year=movie["year"],
                                                 genre=movie["genres"][0],
                                                 rating=movie["rating"],
                                                 votes=movie["votes"],)

        actors = movie["cast"]
        directors = movie["directors"]

        for actor in actors:
            controllers.ActorController.create_actor(full_name=actor["name"],
                                                     movie_id=movie_id)
        for director in directors:
            controllers.DirectorController.create_director(full_name=director["name"],
                                                           movie_id=movie_id)


if __name__ == "__main__":
    films = 20
    fill_data_base(films)
