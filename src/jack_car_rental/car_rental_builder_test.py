from mdp.policy_iterator.value_iterator import ValueIterator
from .builder import CarRentalBuilder
import unittest
from .car_rental_factory import car_rental_factory, car_rental_ext_factory


class CarRentalBuilderTest(unittest.TestCase):
    def test_improve_policy1(self):

        builder = CarRentalBuilder(car_rental_factory.get())
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

    def test_improve_policy_value_iteration(self):

        builder = CarRentalBuilder(car_rental_factory.get(), ValueIterator)
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

    def test_improve_policy_extend(self):

        builder = CarRentalBuilder(car_rental_ext_factory.car_rentals)
        builder.policy_iterate()

        stats = builder.stats
        values = builder.get_values()
        for i in range(len(stats)):
            print(*stats[i])
        for i in range(len(values)):
            print(*values[i])

        builder.stats_to_2d()
        self.assertEqual([5], stats[20][0].action_names())
        self.assertEqual([-5], stats[0][20].action_names())
