from mdp.action.gym_action import GymAction, RewardCalculator
from mdp.policy.greedy_policy import GreedyPolicy


class NStepAction(GymAction):
    def __init__(self, discount_factor, gym_value, **kwargs):
        super().__init__(discount_factor, gym_value, **kwargs)

    def update(self, reward_calculator, next_actions, **kwargs):
        time_step = kwargs['time_step']
        evaluated_action_value = 0
        if next_actions:
            next_action = GreedyPolicy().pick_action(next_actions)
            evaluated_action_value = next_action.evaluate()
        reward_calculator = self.reward_calculators[time_step]
        g = reward_calculator.get_reward() + reward_calculator.get_next_discount() * evaluated_action_value
        self.learn(g)
        del self.reward_calculators[time_step]

    def cache_reward(self, reward, step=9e20):
        for rc in self.reward_calculators.values():
            rc.cache_reward(reward, step)

