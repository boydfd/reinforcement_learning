from jack_car_rental.action_state import ActionState
from jack_car_rental.car_rental_ext import CarRentalExt
from mdp.action import Action
from mdp.foreacher.foreacher_2d import Foreacher2D
from .car_rental import CarRental


class CarRentalFactory:
    def __init__(self):
        car_rentals = []
        for i in range(21):
            car_rentals.append([CarRental(i, j, self) for j in range(21)])
        self.car_rentals = car_rentals
        Foreacher2D(car_rentals, 21, 21).foreach(lambda car_rental: car_rental.init_actions())

    def get(self):
        return self.car_rentals


class CarRentalExtFactory:
    def __init__(self):
        car_rentals = []
        for i in range(21):
            car_rentals.append([CarRentalExt(i, j, self) for j in range(21)])
        self.car_rentals = car_rentals
        Foreacher2D(car_rentals, 21, 21).foreach(lambda car_rental: car_rental.init_actions())

    def get(self):
        return self.car_rentals

