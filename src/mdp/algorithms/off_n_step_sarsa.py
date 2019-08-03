import itertools

import gym
import numpy as np
from tqdm import tqdm

from blackjack.utility import log
from lib import plotting
from lib.envs.cliff_walking import CliffWalkingEnv
from lib.envs.windy_gridworld import WindyGridworldEnv
from mdp.action.n_step_action import NStepAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.e_greedy_policy import EGreedyPolicy
from mdp.policy.greedy_policy import GreedyPolicy


class OffNStepSarsa(Algorithm):
    def __init__(self, gym_env: gym.Env, n):
        super().__init__(gym_env)
        self.n = n

    def run(self, num_episodes, discount_factor=1, epsilon=0.1, learning_rate=0.5):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=NStepAction, learning_rate=learning_rate)
        stats = plotting.EpisodeStats(
            episode_lengths=np.zeros(num_episodes),
            episode_rewards=np.zeros(num_episodes))
        for i_episode in tqdm(range(num_episodes)):
            states = list()
            state = self.env.reset()
            env_list = list()
            T = 1e10
            update_time = -1
            log.debug('----------------------\n\n')
            for t in itertools.count():
                if t < T:
                    policy = EGreedyPolicy(epsilon)
                    action_state = state.get_next_action_state(policy)
                    b = state.get_action_probability(policy, action_state)
                    pi = state.get_action_probability(EGreedyPolicy(0.1), action_state)
                    ratio = pi / b
                    log.debug('s:{}'.format(state))
                    log.debug('a:{}'.format(action_state))
                    log.debug('b:{0:.2f} pi:{1:.2f} ra:{2:.2f}'.format(b, pi, ratio))
                    action_state.add_reward_calculator(t)
                    # self.env.render()
                    next_state, reward, done, _ = self.env.step(action_state.get_gym_action())
                    log.debug('done: {} reward: {}'.format(done, reward))
                    env_list.append((state, action_state))
                    states.append(next_state)
                    accumulated_time = 0 if update_time + 1 < 0 else update_time + 1
                    for s, a_s in env_list[accumulated_time:]:
                        log.debug('cache for s:{} a:{}'.format(s, a_s))
                        a_s.cache_reward(reward, step=t, one_step_importance_sampling_ratio=ratio)
                    stats.episode_rewards[i_episode] += reward
                    stats.episode_lengths[i_episode] = t
                    if done:
                        T = t + 1
                    else:
                        state = next_state
                update_time = t - self.n + 1
                if update_time >= 0:
                    action_state_update_time = env_list[update_time][1]
                    evaluated_state_index = update_time + self.n - 1
                    if evaluated_state_index < len(states):
                        log.debug('=n')
                        state_update_time = states[evaluated_state_index]
                        action_state_update_time.update(0, state_update_time.get_actions(), time_step=update_time)
                    else:
                        log.debug('<n')
                        action_state_update_time.update(0, None, time_step=update_time)
                if update_time == T - 1:
                    a_ss = [a_s for _, a_s in env_list]
                    for a_s in a_ss:
                        a_s.clear_reward_calculator()
                    break
        return stats


if __name__ == '__main__':
    q_learning = OffNStepSarsa(WindyGridworldEnv(), 2)
    stats = q_learning.run(20000)
    plotting.plot_episode_stats(stats)
    q_learning.show_one_episode()
    # q_learning = NStepSarsa(WindyGridworldEnv(), 8)
    # stats = q_learning.run(50000)
    # plotting.plot_episode_stats(stats)
    # q_learning.show_one_episode()
