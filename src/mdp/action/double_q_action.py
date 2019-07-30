import random

from mdp.action.gym_action import GymAction
from mdp.policy.greedy_policy import GreedyPolicy


class DoubleQAction(GymAction):
    def __init__(self, discount_factor, gym_value, name=None, learning_rate=0.5):
        super().__init__(discount_factor, gym_value, name, learning_rate)
        self.q1 = 0
        self.q2 = 0

    def evaluate(self):
        return self.q1 + self.q2

    def update(self, reward, next_actions, **kwargs):
        random_int = random.randint(0, 1)
        if random_int == 0:
            self.update_q1(reward, next_actions)
        else:
            self.update_q2(reward, next_actions)

    def update_q1(self, reward, next_actions):
        next_action_state = GreedyPolicy(lambda action: action.q2).pick_action(next_actions)
        self.q1 = self.q1 + self.learning_rate * (reward + self.discount_factor * next_action_state.q2 - self.q1)
        self.learning_rate = self.anneal()

    def update_q2(self, reward, next_actions):
        next_action_state = GreedyPolicy(lambda action: action.q1).pick_action(next_actions)
        self.q2 = self.q2 + self.learning_rate * (reward + self.discount_factor * next_action_state.q1 - self.q2)
        self.learning_rate = self.anneal()

