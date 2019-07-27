import itertools

import gym

from mdp.policy.greedy_policy import GreedyPolicy


class Algorithm:
    def __init__(self, gym_env: gym.Env, action_evaluator=lambda a: a.evaluate()):
        self.gym_env = gym_env
        self.env = None
        self.action_evaluator = action_evaluator

    def show_one_episode(self):
        state = self.env.reset()
        for t in itertools.count():
            self.env.render()
            action_state = state.get_next_action_state(GreedyPolicy(self.action_evaluator))
            next_state, reward, done, _ = self.env.step(action_state.get_gym_action())
            if done:
                self.env.render()
                break
            state = next_state
