from tqdm import tqdm

from lib.envs.blackjack import BlackjackEnv
from mdp.action.mc_offline_action import McOfflineAction
from mdp.algorithms.algorithm import Algorithm
from mdp.gym_env import Env
from mdp.policy.greedy_policy import GreedyPolicy
from mdp.policy.random_policy import RandomPolicy


class McOfflinePolicy(Algorithm):
    def run(self, num_episodes, discount_factor=1, epsilon=0.1):
        self.env = Env(self.gym_env, discount_factor, epsilon, action_type=McOfflineAction)
        for _ in tqdm(range(num_episodes)):
            action_states = self.generate_one_episode_action_states_by_policy(RandomPolicy())
            # for s in states:
            #     s.update_reward()
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

    def get_result(self):
        a_list = [[1 for _ in range(11)] for _ in range(10)]
        no_a_list = [[1 for _ in range(11)] for _ in range(10)]
        for item in [state.get_result() for state in self.env.states.states.values()]:
            state = item[0]
            action = item[1]
            player, dealer, usable_a = state[0], state[1], state[2]
            if player > 21:
                continue
            if usable_a:
                a_list[dealer - 1][player - 11] = action
            else:
                no_a_list[dealer - 1][player - 11] = action
        return a_list + no_a_list


if __name__ == '__main__':
    iterator = McOfflinePolicy(BlackjackEnv())
    iterator.run(3000000)
    iterator.show_one_episode()
