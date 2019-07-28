from tqdm import tqdm

from lib.envs.cliff_walking import CliffWalkingEnv
from mdp.action.mc_offline_action import McOfflineAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.greedy_policy import GreedyPolicy
from mdp.policy.random_policy import RandomPolicy


class McOfflinePolicy(Algorithm):
    def run(self, num_episodes, discount_factor=0.8, epsilon=0.1):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=McOfflineAction)
        for _ in tqdm(range(num_episodes)):
            action_states = self.generate_one_episode_action_states_by_policy(RandomPolicy())
            w = 1
            g = 0
            for action_state in reversed(action_states):
                state, action_state, reward = action_state
                g = discount_factor * g + reward
                action_state.update_c(w)
                action_state.update_q(g, w)
                action = state.get_next_action_state(GreedyPolicy())
                if action != action_state:
                    break
                w = w * (1 / 0.5)
        return state

    def generate_one_episode_action_states_by_policy(self, policy):
        actions = []
        state = self.env.reset()
        for t in range(100):
            action = state.get_next_action_state(policy)
            next_state, reward, done, _ = self.env.step(action.get_gym_action())
            actions.append((state, action, reward))
            if done:
                break
            state = next_state
        return actions


if __name__ == '__main__':
    q_learning = McOfflinePolicy(CliffWalkingEnv())
    q_learning.run(500000)
    # plotting.plot_episode_stats(stats)
    q_learning.show_one_episode()

