from gambler import capital_factory
from mdp.iterator.value_iterator import ValueIterator
from .builder import CapitalBuilder
import unittest


class CarRentalBuilderTest(unittest.TestCase):
    def test_improve_policy1(self):

        builder = CapitalBuilder(capital_factory.capitals)
        builder.policy_iterate()

        stats = builder.stats

        self.assertEqual([50], stats[50].action_names())
        self.assertEqual([25], stats[25].action_names())

