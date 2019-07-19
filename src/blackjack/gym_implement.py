from collections import defaultdict

import numpy as np
from tqdm import tqdm

from lib import plotting
from lib.envs.blackjack import BlackjackEnv
from mdp.gym_env import Env


class PolicyIterator:
    def __init__(self):
        self.env = None

    def run(self, num_episodes, discount_factor=1, epsilon=0.1):
        self.env = Env(BlackjackEnv(), discount_factor, epsilon)
        for _ in tqdm(range(num_episodes)):
            states = []
            state = self.env.reset()
            for t in range(100):
                action = state.get_next_action()
                next_state, reward, done, _ = self.env.step(action)
                state.cache_reward(reward)
                if state not in states:
                    states.append(state)
                if done:
                    break
                state = next_state
            for s in states:
                s.update_reward()


if __name__ == '__main__':
    iterator = PolicyIterator()
    iterator.run(500000)
    Q = iterator.env.to_v()
    print(Q)
    V = defaultdict(float)
    for state, actions in Q.items():
        action_value = np.max(actions)
        V[state] = action_value
    plotting.plot_value_function(V, title="Optimal Value Function")
