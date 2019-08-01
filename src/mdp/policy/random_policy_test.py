from mock import Mock, MagicMock
import numpy as np

from mdp.policy.random_policy import RandomPolicy
from test_base import TestBase


class RandomPolicyTest(TestBase):
    def test_should_return_correct_probabilities(self):
        action1 = Mock()
        action2 = Mock()
        action1.evaluate = MagicMock(return_value=1)
        action2.evaluate = MagicMock(return_value=2)
        actual = RandomPolicy().action_to_probability([action1, action2])
        self.assertAlmostEqual(0.5, actual[action1])
        self.assertAlmostEqual(0.5, actual[action2])

