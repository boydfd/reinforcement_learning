from random import random, choices
from typing import List

import numpy as np

from blackjack.utility import log
from mdp.action.gym_action import GymAction
from mdp.policy.greedy_policy import GreedyPolicy
from mdp.policy.policy import Policy


class GymState:
    def __init__(self, state, available_actions: List[GymAction], name=None, epsilon=None):
        self.state = state
        if len(available_actions) == 0:
            raise RuntimeError('available should not be empty')
        self.available_actions = available_actions
        self.value = 0
        self.next_value = 0
        self.next_policy = None
        self.name = name
        self.current_policy = {}
        self.episode_cache_actions = set()
        self.epsilon = epsilon

    def get_actions(self):
        return self.available_actions

    def get_next_action_state(self, policy: Policy) -> GymAction:
        return policy.pick_action(self.available_actions)

    def get_next_action(self):
        action = self._get_next_action()
        if action not in self.episode_cache_actions:
            self.episode_cache_actions.add(action)
        return action.get_gym_action()

    def cache_reward(self, episode_reward, step):
        for action in self.episode_cache_actions:
            action.cache_reward(episode_reward, step)

    def update_reward(self):
        for action in self.episode_cache_actions:
            action.update_reward()
        self.episode_cache_actions = set()

    def choose_random_policy(self):
        actions = self.available_actions
        self.next_policy = actions[random.randint(0, len(actions) - 1)]
        log.debug('choose random:{}'.format(self.next_policy))

    def _get_next_action(self):
        action = self._choose_next_action()
        log.debug('choose:{}'.format(self.next_policy))
        return action

    def _choose_next_action(self):
        reward = -10e10
        action_max = -1
        for i, action in enumerate(self.available_actions):
            action_reward = action.evaluate()
            if action_reward > reward:
                reward = action_reward
                action_max = i

        action_length = len(self.available_actions)
        single_prob = self.epsilon / action_length
        actions = [single_prob for _ in range(action_length)]
        actions[action_max] += 1 - self.epsilon
        return self.available_actions[choices(range(action_length), actions)[0]]

    def to_v(self):
        return np.array([action.evaluate() for action in self.available_actions])

    def get_result(self):
        return self.state, GreedyPolicy().pick_action(self.available_actions).get_gym_action()

    def __str__(self):
        return '{}: {{a-> {}}}'.format(self.state, self.available_actions)

    def __repr__(self):
        return self.__str__()
