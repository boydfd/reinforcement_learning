from typing import List

from mdp.action import Action
from mdp.state import State


class Environment:
    def __init__(self, stats: List[State], initial_stat: State):
        self.stats = stats
        self.current_stat = initial_stat

    def take_action(self, action: Action) -> State:
        return None
