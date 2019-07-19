from typing import List


class ScoreCalculator:
    def __init__(self, numbers: List):
        self.numbers = numbers

    def calculate(self):
        return sum(self.numbers) + self.get_extra()

    def get_extra(self):
        if self.have_usable_a():
            return 10
        return 0

    def have_usable_a(self):
        return 1 in self.numbers and sum(self.numbers) <= 11
