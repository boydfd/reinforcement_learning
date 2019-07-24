from tqdm import tqdm

from lib.envs.blackjack import BlackjackEnv
from mdp.gym_env import Env


class McOnline:
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

    def get_result(self):
        a_list = [[1 for _ in range(11)] for _ in range(10)]
        no_a_list = [[1 for _ in range(11)] for _ in range(10)]
        for item in [state.get_result() for state in self.env.states.states.values()]:
            state = item[0]
            action = item[1]
            player, dealer, usable_a = state[0], state[1], state[2]
            if usable_a:
                a_list[dealer - 1][player - 11] = action
            else:
                no_a_list[dealer - 1][player - 11] = action
        return a_list + no_a_list