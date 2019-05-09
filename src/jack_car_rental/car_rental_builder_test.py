from .builder import CarRentalBuilder
import unittest


class CarRentalBuilderTest(unittest.TestCase):
    def test_improve_policy1(self):

        builder = CarRentalBuilder()
        builder.policy_iterate()

        stats = builder.stats
        values = builder.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        builder.stats_to_2d()
        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-4], stats[0][20].action_names())
        # self.assertEqual(['right'], stats[4][2].action_names())
        # self.assertEqual(['left', 'down'], stats[1][4].action_names())
