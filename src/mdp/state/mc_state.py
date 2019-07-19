import math
from typing import Dict, List
import random

from blackjack.utility import log
from mdp.action.first_mc_action import FirstMCAction


class MCState:
    def __init__(self, available_actions: List[FirstMCAction] = None, name=None):
        if available_actions is None:
            available_actions = {}
        self.available_actions = available_actions
        self.value = 0
        self.next_value = 0
        self.next_policy = None
        self.name = name
        self.current_policy = {}

    def get_next_action(self):
        return self.next_policy

    def update_reward(self, episode_reward):
        self.next_policy.update_reward(episode_reward)

    def choose_random_policy(self):
        actions = self.available_actions
        self.next_policy = actions[random.randint(0, len(actions) - 1)]
        log.debug('choose random:{}'.format(self.next_policy))

    def choose_next_policy(self):
        self.next_policy = self._choose_next_action()
        log.debug('choose:{}'.format(self.next_policy))

    def _choose_next_action(self):
        reward = -10e10
        action_max = []
        for action in self.available_actions:
            action_reward = action.evaluate()
            if math.isclose(reward, action_reward, rel_tol=1e-010):
                action_max.append(action)
            if action_reward > reward:
                reward = action_reward
                action_max = [action]
        return action_max[random.randint(0, len(action_max) - 1)]

    def __str__(self):
        reward = -10e10
        action_max = []
        keys = self.available_actions
        for action in keys:
            action_reward = action.evaluate()
            if math.isclose(reward, action_reward, rel_tol=1e-010):
                action_max.append(action)
            if action_reward > reward:
                reward = action_reward
                action_max = [action]
        return '{}: {} -- {} -- next: {}'.format(self.name, keys, action_max, self.next_policy)

    def __repr__(self):
        return self.__str__()
    # def print(self):
    #     actions =  self.available_actions.keys()
    #     log.log('{}: {} -- next: {}'.format(self.name, actions, self.next_policy))
