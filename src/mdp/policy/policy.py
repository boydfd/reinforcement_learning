from typing import List

from mdp.action.gym_action import GymAction


class Policy:
    @classmethod
    def pick_action(cls, actions: List[GymAction]) -> GymAction:
        pass
