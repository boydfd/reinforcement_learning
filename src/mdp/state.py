from .action import Action
from typing import Dict
import math


class State:
    def __init__(self, available_actions: Dict[Action, float] = None, name=None):
        if available_actions is None:
            available_actions = {}
        self.available_actions = available_actions
        self.value = 0
        self.next_value = 0
        self.next_policy = None
        self.name = name

    def add_action(self, action, possibility):
        self.available_actions[action] = possibility

    def reset_possibility(self):
        pass

    def evaluate(self):
        next_value = sum([action.evaluate() * possibility for action, possibility in self.available_actions.items()])
        self.next_value = next_value

    def delta(self):
        return self.next_value - self.value

    def policy_improve(self):
        max_indexes = []
        max_value = float("-infinity")
        for action in self.available_actions.keys():
            evaluate = action.evaluate()
            if math.isclose(evaluate, max_value, rel_tol=1e-05):
                max_indexes.append(action)
            elif evaluate > max_value:
                max_value = evaluate
                max_indexes = [action]
        self.next_policy = max_indexes

    def update_policy(self):
        item_to_delete = [action for action in self.available_actions.keys() if action not in self.next_policy]
        for action in item_to_delete:
            del self.available_actions[action]
        self.reset_possibility()
        return len(item_to_delete) == 0

    def replace_old_value(self):
        self.value = self.next_value

    def __str__(self):
        return '{}:{}'.format(self.value, self.available_actions.keys())

    def __repr__(self):
        return self.__str__()
