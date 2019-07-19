import statistics


class RewardCalculator:
    INIT_REWARD_CACHE_COUNT = 1
    INIT_REWARD_CACHE_VALUE = 0

    def __init__(self, discount_factor):
        self.discount_factor = discount_factor
        self.reward_cache_count = None
        self.reward_cache = None
        self.init()

    def init(self):
        self.reward_cache_count = self.INIT_REWARD_CACHE_COUNT
        self.reward_cache = self.INIT_REWARD_CACHE_VALUE

    def cache_reward(self, reward):
        self.reward_cache += reward * (self.discount_factor ** self.reward_cache_count)
        self.reward_cache_count += 1

    def get_reward(self):
        return self.reward_cache


class FirstMCAction:
    def __init__(self, discount_factor, name=None):
        self.name = name
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
        return self.reward / self.count

    def cache_reward(self, reward):
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
