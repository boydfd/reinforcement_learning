import itertools

import gym
from tqdm import tqdm
import numpy as np

from lib import plotting
from lib.envs.windy_gridworld import WindyGridworldEnv
from mdp.action.gym_action import GymAction
from mdp.action.sarsa_action import SarsaAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.e_greedy_policy import EGreedyPolicy


class Sarsa(Algorithm):
    def run(self, num_episodes, discount_factor=1, epsilon=0.1, learning_rate=0.5):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=SarsaAction, learning_rate=learning_rate)
        stats = plotting.EpisodeStats(
            episode_lengths=np.zeros(num_episodes),
            episode_rewards=np.zeros(num_episodes))
        for i_episode in tqdm(range(num_episodes)):
            state_actions = set()
            state = self.env.reset()
            for t in itertools.count():
                action_state = state.get_next_action_state(EGreedyPolicy(epsilon))
                next_state, reward, done, _ = self.env.step(action_state.get_gym_action())
                if state not in state_actions:
                    state_actions.add(action_state)
                stats.episode_rewards[i_episode] += reward
                stats.episode_lengths[i_episode] = t
                action_state.update(reward, next_state.get_actions(), policy=EGreedyPolicy(epsilon))
                if done:
                    break
                state = next_state

        return stats


if __name__ == '__main__':
    sarsa = Sarsa(WindyGridworldEnv())
    stats = sarsa.run(20000)
    plotting.plot_episode_stats(stats)
    sarsa.show_one_episode()
