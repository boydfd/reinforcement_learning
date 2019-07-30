from mdp.action.gym_action import GymAction


class SarsaAction(GymAction):
    def update(self, reward, next_actions, **kwargs):
        next_q_value = kwargs['policy'].pick_action(next_actions).evaluate()
        g = reward + self.discount_factor * next_q_value
        self.learn(g)
