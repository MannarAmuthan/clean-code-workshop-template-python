from src.movie_rental.Customer import Customer
from src.movie_rental.Movie import Movie
from src.movie_rental.Rental import Rental


def test_characterisation():
    customer: Customer = Customer("BoB")
    customer.add_rental(Rental(Movie("movie-1", Movie.REGULAR), 10))
    customer.add_rental(Rental(Movie("movie-2", Movie.CHILDRENS), 10))
    customer.add_rental(Rental(Movie("movie-3", Movie.NEW_RELEASE), 10))

    assert "Rental Record for BoB\n" \
           "\tmovie-1\t14.0\n" \
           "\tmovie-2\t12.5\n" \
           "\tmovie-3\t30\n" \
           "Amount owed is 56.5\n" \
           "You earned 4 frequent renter points" == customer.statement()


def test_html_statement():
    customer: Customer = Customer("BoB")
    customer.add_rental(Rental(Movie("movie-1", Movie.REGULAR), 10))
    customer.add_rental(Rental(Movie("movie-2", Movie.CHILDRENS), 10))
    customer.add_rental(Rental(Movie("movie-3", Movie.NEW_RELEASE), 10))

    assert "<html><h1>Rental Record for <b>BoB</b></h1></br>" \
           " movie-1 14.0</br>" \
           " movie-2 12.5</br>" \
           " movie-3 30</br>" \
           "Amount owed is <b>56.5</b></br>" \
           "You earned <b>4</b> frequent renter points</html>" == customer.html_statement()



