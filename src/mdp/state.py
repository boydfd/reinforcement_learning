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
        self.current_policy = {}

    def add_action(self, action, possibility):
        self.available_actions[action] = possibility

    def set_current_policy(self, policy):
        self.current_policy = policy

    def sync_policy_and_actions(self):
        self.current_policy = self.available_actions

    def balance_actions(self):
        key_length = len(self.available_actions.keys())
        if key_length == 0:
            return
        action_possibility = 1 / key_length
        for key in self.available_actions.keys():
            self.available_actions[key] = action_possibility

    def balance_policy(self):
        key_length = len(self.current_policy.keys())
        if key_length == 0:
            return
        action_possibility = 1 / key_length
        for key in self.current_policy.keys():
            self.current_policy[key] = action_possibility

    def reset_possibility(self):
        pass

    def evaluate(self):
        next_value = sum([action.evaluate() * possibility for action, possibility in self.current_policy.items()])
        self.next_value = next_value

    def delta(self):
        return self.next_value - self.value

    def policy_improve(self):
        max_indexes = []
        max_value = float("-infinity")
        for action in self.available_actions.keys():
            evaluate = action.evaluate()
            if math.isclose(evaluate, max_value, rel_tol=1e-010):
                max_indexes.append(action)
            elif evaluate > max_value:
                max_value = evaluate
                max_indexes = [action]
        self.next_policy = max_indexes

    def update_policy(self):
        is_policy_stable = set(self.current_policy.keys()).union(set(self.next_policy)) == set(self.next_policy)
        self.current_policy = {action: 1 for action in self.next_policy}
        self.balance_policy()
        return is_policy_stable

    def replace_old_value(self):
        self.value = self.next_value

    def action_names(self):
        return [action.name for action in self.current_policy.keys()]

    def __str__(self):
        return '{}:{}'.format(self.value, list(self.current_policy.keys()))

    def __repr__(self):
        return self.__str__()
