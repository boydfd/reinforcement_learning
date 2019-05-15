import math

from jack_car_rental.params import MAX_CARS, RENT_INCOME_PER_CAR, COST_FOR_MORE_THAN_TEN_CARS, CAR_THRESHOLD


class Location:
    def __init__(self, count, rent_probability, return_probability, name=None):
        self.count = count
        self.count_log = self.count
        self.rent_probability = rent_probability
        self.return_probability = return_probability
        self.name = name

    def get_probability_list(self):
        pass

    def get_rent_probability(self, n):
        probability = self.rent_probability
        return self.poisson(n, probability)

    def get_return_probability(self, n):
        probability = self.return_probability
        return self.poisson(n, probability)

    def calculate_twenty_probabilities(self):
        twenty = [self.get_rent_probability(x) for x in range(MAX_CARS + 1)]
        rest_probability = 1 - sum(twenty)
        twenty[MAX_CARS] += rest_probability
        return twenty

    def calculate_twenty_return_probabilities(self):
        twenty = [self.get_return_probability(x) for x in range(MAX_CARS + 1)]
        rest_probability = 1 - sum(twenty)
        twenty[MAX_CARS] += rest_probability
        return twenty

    def calculate_expectation(self):
        result = self.rent_probabilities()
        return sum([i * p * RENT_INCOME_PER_CAR for i, p in enumerate(result)])

    def calculate_rent_expectation_with_movement(self, movement):
        self.count_log = self.count
        self.count = self.count - movement
        self.count = self.count if self.count <= MAX_CARS else MAX_CARS
        rents = self.rent_probabilities()
        reward = sum([i * p * RENT_INCOME_PER_CAR for i, p in enumerate(rents)])
        # print('{}: {}'.format(result, reward))
        self.count = self.count_log
        return reward

    def rent_probabilities(self):
        probabilities = self.calculate_twenty_probabilities()
        result = probabilities[:self.count + 1]
        result[self.count] = sum(probabilities[self.count:])
        return result

    def calculate_next_probabilities_with_movement(self, movement):
        self.count_log = self.count
        self.count = self.count - movement
        self.count = self.count if self.count <= MAX_CARS else MAX_CARS
        rent_probabilities = self.rent_probabilities()
        return_probabilities = self.calculate_twenty_return_probabilities()

        probabilities = [0] * (MAX_CARS + 1)
        for i, rent in enumerate(rent_probabilities):
            for j, ret in enumerate(return_probabilities):
                remain = self.count - i + j
                remain = MAX_CARS if remain > MAX_CARS else remain
                probabilities[remain] += rent * ret

        self.count = self.count_log
        return probabilities

    def get_extra_fee(self):
        return COST_FOR_MORE_THAN_TEN_CARS if self.count > CAR_THRESHOLD else 0

    @classmethod
    def poisson(cls, n, probability):
        return probability ** n / math.factorial(n) * math.exp(-probability)


if __name__ == '__main__':
    print(Location(3, 3, 3).calculate_next_probabilities_with_movement(-5))
