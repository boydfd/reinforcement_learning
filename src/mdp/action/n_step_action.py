from blackjack.utility import log
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
        log.debug('g: {}'.format(g))
        self._learn(g, reward_calculator.get_importance_sampling_ratio())
        del self.reward_calculators[time_step]

    def _learn(self, g, importance_sampling_ratio):
        # importance_sampling_ratio = 1
        # print(importance_sampling_ratio)
        log.debug('isr: {}'.format(importance_sampling_ratio))
        if importance_sampling_ratio == 0:
            return
        self.q = self.q + self.learning_rate * importance_sampling_ratio * (g - self.q)
        log.debug('q:{} '.format(self.q))
        # self.learning_rate = self.anneal()

    def cache_reward(self, reward, step=9e20, one_step_importance_sampling_ratio=1):
        for rc in self.reward_calculators.values():
            rc.cache_reward(reward, step, one_step_importance_sampling_ratio=one_step_importance_sampling_ratio)

