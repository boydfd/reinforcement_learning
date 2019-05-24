import unittest

from gambler import capital_factory
from mdp.builder import Builder
from mdp.foreacher.foreacher_1d import Foreacher1D
from mdp.policy_iterator.policy_iterator import PolicyIterator
from mdp.printer.foreach_printer import ForeachPrinter


class CarRentalBuilderTest(unittest.TestCase):
    def test_improve_policy1(self):
        capitals = capital_factory.capitals
        foreacher = Foreacher1D(capitals, 101)
        printer = ForeachPrinter(capitals, foreacher)
        iterator = PolicyIterator(foreacher, printer)
        builder = Builder(iterator)
        builder.policy_iterate()

        self.assertEqual([50], capitals[50].action_names())
        self.assertEqual([25], capitals[25].action_names())
