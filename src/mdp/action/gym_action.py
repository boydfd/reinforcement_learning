class GymAction:
    def __init__(self, discount_factor, gym_value, name=None, learning_rate=0.5):
        self.discount_factor = discount_factor
        self.gym_value = gym_value
        self.q = 0
        self.learning_rate = learning_rate
        self.name = name

    def update(self, reward, next_actions):
        pass

    def evaluate(self):
        return self.q

    def get_gym_action(self):
        return self.gym_value
