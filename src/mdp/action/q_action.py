from mdp.action.gym_action import GymAction
from mdp.policy.greedy_policy import GreedyPolicy


class QAction(GymAction):
    def update(self, reward, next_actions):
        next_q_value = GreedyPolicy().pick_action(next_actions).evaluate()
        self.q = self.q + self.learning_rate * (reward + self.discount_factor * next_q_value - self.q)

