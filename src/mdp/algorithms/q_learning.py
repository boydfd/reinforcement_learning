import itertools

import gym
import numpy as np
from tqdm import tqdm

from lib import plotting
from lib.envs.cliff_walking import CliffWalkingEnv
from mdp.action.q_action import QAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.e_greedy_policy import EGreedyPolicy


class QLearning(Algorithm):
    def run(self, num_episodes, discount_factor=1, epsilon=0.1, learning_rate=0.5):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=QAction, learning_rate=learning_rate)
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
                action_state.update(reward, next_state.get_actions())
                if done:
                    break
                state = next_state

        return stats


if __name__ == '__main__':
    q_learning = QLearning(CliffWalkingEnv())
    stats = q_learning.run(200)
    plotting.plot_episode_stats(stats)
    q_learning.show_one_episode()

