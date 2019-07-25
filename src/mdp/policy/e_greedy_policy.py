import random

from mdp.policy.policy import Policy


class EGreedyPolicy(Policy):
    def __init__(self, epsilon, evaluate=lambda action: action.evaluate()):
        super().__init__(evaluate)
        self.epsilon = epsilon

    def pick_action(self, actions):
        reward = -10e10
        action_max = -1
        for i, action in enumerate(actions):
            action_reward = self.evaluate_action(action)
            if action_reward > reward:
                reward = action_reward
                action_max = i

        action_length = len(actions)
        single_prob = self.epsilon / action_length
        actions_pob = [single_prob for _ in range(action_length)]
        actions_pob[action_max] += 1 - self.epsilon
        return actions[random.choices(range(action_length), actions_pob)[0]]

