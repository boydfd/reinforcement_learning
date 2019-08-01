from unittest.mock import patch, Mock, MagicMock
import numpy as np

from mdp.policy.e_greedy_policy import EGreedyPolicy
from test_base import TestBase


class EGreedyPolicyTest(TestBase):
    def test_should_return_correct_probabilities(self):
        action1 = Mock()
        action2 = Mock()
        action1.evaluate = MagicMock(return_value=1)
        action2.evaluate = MagicMock(return_value=2)
        actual = EGreedyPolicy(0.1).action_to_probability([action1, action2])
        self.assertAlmostEquals(0.95, actual[action2])
        self.assertAlmostEquals(0.05, actual[action1])
