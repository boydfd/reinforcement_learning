from jack_car_rental.car_rental_ext import CarRentalExt
from .car_rental import CarRental


class CarRentalFactory:
    def __init__(self):
        car_rentals = []
        for i in range(21):
            car_rentals.append([CarRental(i, j) for j in range(21)])
        self.car_rentals = car_rentals


class CarRentalExtFactory:
    def __init__(self):
        car_rentals = []
        for i in range(21):
            car_rentals.append([CarRentalExt(i, j) for j in range(21)])
        self.car_rentals = car_rentals

def action_state(result, capital, i):
    tail = result[capital.count - i]
    head = result[capital.count + i]
    return ActionState({
        tail: 0.6,
        head: 0.4,
    })


def recalculate_actions():
    car_rentals = []
    for i in range(21):
        car_rentals.append([CarRental(i, j) for j in range(21)])
    for car_rental in car_rentals:
        max_move = 5 if car_rental.first.count >= 5 else car_rental.first.count
        min_move = -5 if -car_rental.second.count <= -5 else -car_rental.second.count
        car_rental.available_actions = {
            car_rental.get_action(movement): 1 for movement in range(min_move, max_move + 1)
        }
        car_rental.balance_actions()
        car_rental.config_actions(available_actions)
    return car_rentals

car_rental_factory = CarRentalFactory()
car_rental_ext_factory = CarRentalExtFactory()
