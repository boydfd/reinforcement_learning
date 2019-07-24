from mdp.action.gym_action import GymAction


class McOfflineAction(GymAction):
    def __init__(self, discount_factor, gym_value, name=None, learning_rate=0.5):
        super().__init__(discount_factor, gym_value, name, learning_rate=0.5)
        self.name = name
        self.c = 0
        self.q = 0

    def evaluate(self):
        return self.q

    def update_c(self, w):
        self.c = self.c + w

    def update_q(self, g, w):
        self.q = self.q + w / self.c * (g - self.q)

