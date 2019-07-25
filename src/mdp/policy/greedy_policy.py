from mdp.action.gym_action import GymAction
from mdp.policy.policy import Policy


class GreedyPolicy(Policy):
    def pick_action(self, actions) -> GymAction:
        max_action = None
        value = -9e9
        for action in actions:
            evaluate = self.evaluate_action(action)
            if evaluate > value:
                max_action = action
                value = evaluate
        return max_action
