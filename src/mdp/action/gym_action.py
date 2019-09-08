from blackjack.utility import log


class RewardCalculator:
    INIT_REWARD_CACHE_COUNT = 1
    INIT_REWARD_CACHE_VALUE = 0

    def __init__(self, discount_factor, initial_time_step=0):
        self.discount_factor = discount_factor
        self.reward_cache_count = None
        self.reward_cache = None
        self.initial_time_step = initial_time_step
        self.importance_sampling_ratio = 1
        self.init()

    def init(self):
        self.reward_cache_count = self.INIT_REWARD_CACHE_COUNT
        self.reward_cache = self.INIT_REWARD_CACHE_VALUE

    def cache_reward(self, reward, time_step=9e20, **kwargs):
        one_step_importance_sampling_ratio = kwargs['one_step_importance_sampling_ratio']
        log.debug('isr: {:.2f} ->'.format(self.importance_sampling_ratio))
        self.importance_sampling_ratio *= one_step_importance_sampling_ratio
        log.debug('isr: {:.2f}'.format(self.importance_sampling_ratio))
        if self.initial_time_step <= time_step:
            # print('cache {} {} {}'.format(self.initial_time_step, time_step, reward))
            self.reward_cache += reward * (self.discount_factor ** self.reward_cache_count)
            self.reward_cache_count += 1

    def get_importance_sampling_ratio(self):
        return self.importance_sampling_ratio

    def get_next_discount(self):
        return self.discount_factor ** (self.reward_cache_count + 1)

    def get_reward(self):
        return self.reward_cache


class GymAction:
    def __init__(self, discount_factor, gym_value, name=None, learning_rate=0.5, **kwargs):
        self.discount_factor = discount_factor
        self.gym_value = gym_value
        self.q = 0
        self.learning_rate = learning_rate
        self.name = name
        self.reward_calculators = {}

    def cache_reward(self, reward, step=0, one_step_importance_sampling_ratio=1):
        pass

    def learn(self, g):
        self.q = self.q + self.learning_rate * (g - self.q)
        self.learning_rate = self.anneal()

    def anneal(self):
        if self.learning_rate > 0.1:
            return self.learning_rate * 0.99
        else:
            return self.learning_rate

    def update(self, reward, next_actions, **kwargs):
        pass

    def evaluate(self):
        return self.q

    def get_gym_action(self):
        return self.gym_value

    def add_reward_calculator(self, time_step):
        self.reward_calculators[time_step] = RewardCalculator(self.discount_factor, time_step)

    def clear_reward_calculator(self):
        self.reward_calculators = {}

    def __str__(self):
        return '{}:{}'.format(self.get_gym_action(), self.evaluate())

    def __repr__(self):
        return self.__str__()
