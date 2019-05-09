from .car_rental import CarRental


class CarRentalFactory:
    def __init__(self):
        car_rentals = []
        for i in range(21):
            car_rentals.append([CarRental(i, j) for j in range(21)])
        self.car_rentals = car_rentals


car_rental_factory = CarRentalFactory()
