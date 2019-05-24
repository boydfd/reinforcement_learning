import unittest

from mdp.evaluator.inplace_evaluator import InplaceEvaluator
from mdp.policy_iterator.policy_iterator import PolicyIterator
from mdp.policy_iterator.value_iterator import ValueIterator
from .builder import build, build_extension


class CarRentalBuilderTest(unittest.TestCase):
    def test_improve_policy1(self):
        foreacher, printer, stats = build()
        policy_iterator = PolicyIterator(foreacher, printer)
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-4], stats[0][20].action_names())

    def test_improve_policy_value_iteration(self):

        foreacher, printer, stats = build()
        policy_iterator = ValueIterator(foreacher, printer)
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-4], stats[0][20].action_names())

    def test_improve_policy_value_iteration_evaluate_inplace(self):

        foreacher, printer, stats = build()
        policy_iterator = ValueIterator(foreacher, printer, InplaceEvaluator(foreacher))
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-4], stats[0][20].action_names())

    def test_improve_policy_extend(self):

        foreacher, printer, stats = build_extension()
        policy_iterator = PolicyIterator(foreacher, printer)
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-5], stats[0][20].action_names())
        # 19.17 s

    def test_improve_policy_extend_value_iteration(self):

        foreacher, printer, stats = build_extension()
        policy_iterator = ValueIterator(foreacher, printer)
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-5], stats[0][20].action_names())
        # 8.1 s

    def test_improve_policy_extend_value_iteration_inplace(self):

        foreacher, printer, stats = build_extension()
        policy_iterator = ValueIterator(foreacher, printer, InplaceEvaluator(foreacher))
        policy_iterator.iterate()

        values = printer.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-5], stats[0][20].action_names())
        # 4.9 s
