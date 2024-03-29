from mdp.action.gym_action import GymAction, RewardCalculator


class FirstMCAction(GymAction):
    def __init__(self, discount_factor, gym_value, **kwargs):
        super().__init__(discount_factor, gym_value, **kwargs)

    def cache_reward(self, reward, step=0, **kwargs):
        index = min(self.reward_calculators.keys())
        self.reward_calculators[index].cache_reward(reward, step, kwargs)

    def update(self, reward, next_actions, **kwargs):
        index = min(self.reward_calculators.keys())
        g = self.reward_calculators[index].get_reward()
        self.learn(g)

