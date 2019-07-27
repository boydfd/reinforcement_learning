from mdp.gym_env import Env


class BlackjackGetter:
    def __init__(self, env: Env):
        self.env = env

    def get(self):
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
