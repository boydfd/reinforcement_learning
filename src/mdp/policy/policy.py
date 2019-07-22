from typing import List

from mdp.action.first_mc_action import FirstMCAction


class Policy:
    @classmethod
    def pick_action(cls, actions: List[FirstMCAction]) -> FirstMCAction:
        pass
