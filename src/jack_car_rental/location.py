import math


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
        return self.get_probability(n, probability)

    def get_return_probability(self, n):
        probability = self.return_probability
        return self.get_probability(n, probability)

    def calculate_twenty_probabilities(self):
        twenty = [self.get_rent_probability(x) for x in range(21)]
        rest_probability = 1 - sum(twenty)
        twenty[20] += rest_probability
        return twenty

    def calculate_twenty_return_probabilities(self):
        twenty = [self.get_return_probability(x) for x in range(21)]
        rest_probability = 1 - sum(twenty)
        twenty[20] += rest_probability
        return twenty

    def calculate_expectation(self):
        result = self.rent_probabilities()
        rent_fee_per_car = 10
        return sum([i * p * rent_fee_per_car for i, p in enumerate(result)])

    def calculate_expectation_with_movement(self, movement):
        self.count_log = self.count
        self.count = self.count - movement
        self.count = self.count if self.count <= 20 else 20
        result = self.rent_probabilities()
        rent_fee_per_car = 10
        reward = sum([i * p * rent_fee_per_car for i, p in enumerate(result)])
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
        self.count = self.count if self.count <= 20 else 20
        rent_probabilities = self.rent_probabilities()
        return_probabilities = self.calculate_twenty_return_probabilities()

        probabilities = [0] * 21
        for i, rent in enumerate(rent_probabilities):
            for j, ret in enumerate(return_probabilities):
                remain = self.count - i + j
                remain = 20 if remain > 20 else remain
                probabilities[remain] += rent * ret

        self.count = self.count_log
        return probabilities

    @classmethod
    def get_probability(cls, n, probability):
        return probability ** n / math.factorial(n) * math.exp(-probability)


if __name__ == '__main__':
    print(Location(3, 3, 3).calculate_next_probabilities_with_movement(-5))
