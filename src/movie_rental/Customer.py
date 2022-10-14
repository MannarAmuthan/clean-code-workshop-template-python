from typing import Callable

from src.movie_rental.Movie import Movie
from src.movie_rental.Rental import Rental


class Customer:
    name: str
    rentals: list[Rental]

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_name(self) -> str:
        return self.name

    def __frequent_renter_point(self) -> int:
        frequent_renter_points = len(self.rentals)
        for rental in self.rentals:
            if (rental.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
                    (rental.get_days_rented() > 1):
                frequent_renter_points += 1
        return frequent_renter_points

    def __total_amount(self):
        total_amount: float = 0
        for rental in self.rentals:
            rental_amount = self.__rental_amount(rental)
            total_amount += rental_amount
        return total_amount

    def __rental_amount(self, rental: Rental) -> float:
        this_amount: float = 0
        if rental.get_movie().get_price_code() == Movie.REGULAR:
            this_amount += 2
            if rental.get_days_rented() > 2:
                this_amount += (rental.get_days_rented() - 2) * 1.5
                return this_amount
        elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            this_amount += rental.get_days_rented() * 3
            return this_amount
        elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
            this_amount += 2
            if rental.get_days_rented() > 3:
                this_amount += (rental.get_days_rented() - 3) * 1.5
                return this_amount

    def __construct_statement(self, formatter: Callable[[Rental], str]) -> str:
        formatted_result = ""
        for rental in self.rentals:
            formatted_result += formatter(rental)
        return formatted_result

    def statement(self) -> str:
        total_amount: float = self.__total_amount()
        result: str = "Rental Record for " + self.get_name() + "\n"

        result += self.__construct_statement(
            lambda rental: "\t" + rental.get_movie().get_title() + "\t" + \
                           str(self.__rental_amount(rental)) + "\n")

        frequent_renter_points: int = self.__frequent_renter_point()

        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + \
                  " frequent renter points"

        return result

    def html_statement(self):
        total_amount: float = self.__total_amount()
        result = self.__construct_statement(
            lambda rental: f" {rental.get_movie().get_title()} {self.__rental_amount(rental)}</br>")

        return f"<html><h1>Rental Record for <b>{self.name}</b></h1></br>{result}" \
               f"Amount owed is <b>{total_amount}</b></br>" \
               f"You earned <b>{self.__frequent_renter_point()}</b> frequent renter points</html>"
