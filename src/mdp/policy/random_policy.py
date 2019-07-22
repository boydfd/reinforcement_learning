import random


class RandomPolicy:
    @classmethod
    def pick_action(cls, actions):
        return actions[random.randint(0, len(actions) - 1)]
