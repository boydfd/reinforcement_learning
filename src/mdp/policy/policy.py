from typing import List

from mdp.action.gym_action import GymAction


class Policy:
    def __init__(self, evaluate=lambda action: action.evaluate()):
        self.evaluate = evaluate

    def pick_action(self, actions: List[GymAction]) -> GymAction:
        pass

    def evaluate_action(self, action):
        return self.evaluate(action)
