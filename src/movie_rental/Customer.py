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

    def statement(self) -> str:
        total_amount: float = 0.0
        frequent_renter_points: int = 0
        result: str = "Rental Record for " + self.get_name() + "\n"
        for each in self.rentals:
            this_amount: float = 0
            # determine amounts for each line
            match each.get_movie().get_price_code():
                case Movie.REGULAR:
                    this_amount += 2
                    if each.get_days_rented() > 2:
                        this_amount += (each.get_days_rented() - 2) * 1.5
                case Movie.NEW_RELEASE:
                    this_amount += each.get_days_rented() * 3
                case Movie.CHILDRENS:
                    this_amount += 2
                    if each.get_days_rented() > 3:
                        this_amount += (each.get_days_rented() - 3) * 1.5
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
                    (each.get_days_rented() > 1):
                frequent_renter_points += 1
            # show figure for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + \
                      str(this_amount) + "\n"
            total_amount += this_amount
        # add footer lines result
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + \
                  " frequent renter points"
        return result
