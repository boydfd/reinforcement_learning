from mdp.action.gym_action import GymAction
from mdp.policy.e_greedy_policy import EGreedyPolicy
from mdp.policy.policy import Policy


class GreedyPolicy(Policy):
    policy = EGreedyPolicy(0)

    def probabilities(self, actions):
        return self.policy.probabilities(actions)
