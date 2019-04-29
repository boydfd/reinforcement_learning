from typing import Dict

from .state import State


class ActionState:
    def __init__(self, next_states: Dict[State, float]):
        self.next_states = next_states

    def add_action_state(self, action_state, possibility):
        self.next_states[action_state] = possibility

    def evaluate(self):
        return sum([state.value * possibility for state, possibility in self.next_states.items()])
