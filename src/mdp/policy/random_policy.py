import random

from mdp.policy.policy import Policy


class RandomPolicy(Policy):
    def probabilities(self, actions):
        length = len(actions)
        return [1 / length] * length
