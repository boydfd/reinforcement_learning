from mdp.action.gym_action import GymAction, RewardCalculator


class FirstMCAction(GymAction):
    def __init__(self, discount_factor, gym_value, **kwargs):
        super().__init__(discount_factor, gym_value, **kwargs)
        self.next_states = {}
        self.reward = 0
        self.count = 0
        self.reward_calculator = RewardCalculator(discount_factor)

    def found_next_state(self, next_state, reward):
        existed_reward = self.next_states[next_state]
        self.next_states[next_state] = existed_reward if existed_reward else reward

    def evaluate(self):
        if self.count == 0:
            return 0
        self.q = self.reward / self.count
        return self.q

    def cache_reward(self, reward, step=0):
        self.reward_calculator.cache_reward(reward)

    def update_reward(self):
        self.count += 1
        self.reward += self.reward_calculator.get_reward()
        self.reward_calculator.init()

    def get_average_reward(self):
        return self.reward / self.count

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.evaluate(), self.count)

    def __repr__(self):
        return self.__str__()
