from jack_car_rental.car_rental_factory import CarRentalFactory, CarRentalExtFactory
from jack_car_rental.params import MAX_CARS
from jack_car_rental.printer import Printer

from mdp.foreacher.foreacher_2d import Foreacher2D


def build():
    max_count = MAX_CARS + 1
    row_length = max_count
    column_length = max_count
    rentals = CarRentalFactory().car_rentals
    foreacher = Foreacher2D(
        rentals, row_length, column_length)
    printer = Printer(rentals)
    return foreacher, printer, rentals


def build_extension():
    max_count = MAX_CARS + 1
    row_length = max_count
    column_length = max_count
    rentals = CarRentalExtFactory().car_rentals
    foreacher = Foreacher2D(
        rentals, row_length, column_length)
    printer = Printer(rentals)
    return foreacher, printer, rentals

