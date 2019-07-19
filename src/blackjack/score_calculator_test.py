from unittest import TestCase

from blackjack.score_calculator import ScoreCalculator


class ScoreCalculatorTest(TestCase):
    def test_calculate(self):
        self.assertEqual(13, ScoreCalculator([1, 2]).calculate())
        self.assertEqual(21, ScoreCalculator([1, 10]).calculate())
        self.assertEqual(11, ScoreCalculator([1]).calculate())
        self.assertEqual(20, ScoreCalculator([10, 10]).calculate())

    def test_have_usable_a(self):
        self.assertEqual(True, ScoreCalculator([1, 2]).have_usable_a())
        self.assertEqual(True, ScoreCalculator([1, 10]).have_usable_a())
        self.assertEqual(True, ScoreCalculator([1, 1, 9]).have_usable_a())
        self.assertEqual(True, ScoreCalculator([1]).have_usable_a())
        self.assertEqual(False, ScoreCalculator([10, 10, 1]).have_usable_a())
