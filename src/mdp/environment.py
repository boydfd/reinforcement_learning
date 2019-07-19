from typing import List

from mdp.action import Action
from mdp.action_state import ActionState
from mdp.state.mc_state import MCState
from mdp.state.state import State


class Environment:
    def __init__(self, stats: List[State], initial_stat: MCState):
        self.stats = stats
        self.current_stat = initial_stat
        self.state_gone_through = [self.current_stat]

    def go_through_state(self, state):
        self.state_gone_through.append(state)
    # def execute_one_episode(self):
    #     while True:
    #         next_state = self.get_next_state()
    #         if self.is_end_for(next_state):
    #             break
    #     self.update_reward(self.get_reward())
    #
    # def get_next_state(self):
    #     action = self.current_stat.get_next_action()
    #     next_state = self._get_next_state(self.current_stat, action)
    #     ActionState(action)
    #     return next_state
    #
    # def is_end_for(self, next_state):
    #     return True
    #
    # def get_return(self):
    #     pass


    # def get_reward(self):
    #     pass
    #
    # def update_reward(self, episode_reward):
    #     for state in self.state_passed:
    #         state.update_reward(episode_reward)
