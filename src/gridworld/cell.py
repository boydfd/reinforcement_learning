from typing import Dict

from gridworld.action import noop_action
from mdp.action import Action
from mdp.state import State


class Cell(State):
    def __init__(self, available_actions: Dict[Action, float] = None, name=None, ):
        super().__init__(available_actions, name)

    def add_action(self, action, possibility=None):
        action_possibility = 1 / (len(self.available_actions.keys()) + 1)
        self.available_actions[action] = 0
        for key in self.available_actions.keys():
            self.available_actions[key] = action_possibility

    def reset_possibility(self):
        keys_ = len(self.available_actions.keys())
        if keys_ == 0:
            return
        action_possibility = 1 / keys_
        for key in self.available_actions.keys():
            self.available_actions[key] = action_possibility

    def action_names(self):
        return [action.name for action in self.available_actions.keys()]


class EndCell(Cell):
    def __init__(self):
        available_actions = {noop_action: 1}
        super().__init__(available_actions)

    def add_action(self, action, possibility=None):
        pass
