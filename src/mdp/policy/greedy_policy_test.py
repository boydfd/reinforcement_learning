from mock import Mock, MagicMock

from mdp.action.gym_action import GymAction
from mdp.policy.e_greedy_policy import EGreedyPolicy
from mdp.policy.greedy_policy import GreedyPolicy
from mdp.policy.policy import Policy
from test_base import TestBase


class GreedyPolicyTest(TestBase):
    def test_should_return_correct_probabilities(self):
        action1 = Mock()
        action2 = Mock()
        action1.evaluate = MagicMock(return_value=1)
        action2.evaluate = MagicMock(return_value=2)
        actual = GreedyPolicy(0.1).action_to_probability([action1, action2])
        self.assertAlmostEqual(1, actual[action2])
        self.assertAlmostEqual(0, actual[action1])

