from tqdm import tqdm

from lib.envs.blackjack import BlackjackEnv
from lib.envs.cliff_walking import CliffWalkingEnv
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env


class McOnline(Algorithm):
    def run(self, num_episodes, discount_factor=1, epsilon=0.1):
        self.env = Env(self.gym_env, discount_factor, epsilon)
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
    q_learning = McOnline(CliffWalkingEnv())
    q_learning.run(500)
    # plotting.plot_episode_stats(stats)
    q_learning.show_one_episode()
