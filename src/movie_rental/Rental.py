from src.movie_rental.Movie import Movie


class Rental:
    movie: Movie
    days_rented: int

    def __init__(self, movie: Movie, days_rented: int):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_movie(self) -> Movie:
        return self.movie
