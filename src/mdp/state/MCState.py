from typing import Dict

from mdp.action import Action


class MCState:
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


