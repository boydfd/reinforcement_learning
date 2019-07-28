import itertools

from tqdm import tqdm

from lib.envs.blackjack import BlackjackEnv
from lib.envs.cliff_walking import CliffWalkingEnv
from mdp.action.first_mc_action import FirstMCAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.e_greedy_policy import EGreedyPolicy


class McOnline(Algorithm):
    def run(self, num_episodes, discount_factor=1, epsilon=0.3):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=FirstMCAction)
        for _ in tqdm(range(num_episodes)):
            action_states = []
            state = self.env.reset()
            states = [state]
            for t in range(100):
                action_state = state.get_next_action_state(EGreedyPolicy(epsilon))
                next_state, reward, done, _ = self.env.step(action_state.get_gym_action())
                action_state.add_reward_calculator(t)
                if state not in states:
                    states.append(state)
                if action_state not in action_states:
                    action_states.append(action_state)
                for a_s in action_states:
                    a_s.cache_reward(reward, t)
                if done:
                    break
                state = next_state
            for i, s in enumerate(action_states):
                s.update(0, [], {'time_step': i})
            for a_s in action_states:
                a_s.clear_reward_calculator()



if __name__ == '__main__':
    q_learning = McOnline(CliffWalkingEnv())
    q_learning.run(5000)
    # plotting.plot_episode_stats(stats)
    q_learning.show_one_episode()
