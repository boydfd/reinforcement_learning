import random
from typing import List

from mdp.action.gym_action import GymAction


class Policy:
    def __init__(self, evaluate=lambda action: action.evaluate()):
        self.evaluate = evaluate

    def pick_action(self, actions):
        action_length = len(actions)
        actions_prob = self.probabilities(actions)
        return actions[random.choices(range(action_length), actions_prob)[0]]

    def action_to_probability(self, actions):
        return self.convert_into_action_to_probability(actions, self.probabilities(actions))

    def evaluate_action(self, action):
        return self.evaluate(action)

    def probabilities(self, actions):
        pass

    @classmethod
    def convert_into_action_to_probability(cls, actions, prob):
        return dict(zip(actions, prob))
