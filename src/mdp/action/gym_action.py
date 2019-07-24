class GymAction:
    def __init__(self, discount_factor, gym_value, name=None, learning_rate=0.5):
        self.discount_factor = discount_factor
        self.gym_value = gym_value
        self.q = 0
        self.learning_rate = learning_rate
        self.name = name

    def update(self, reward, next_q_value):
        self.q = self.q + self.learning_rate * (reward + self.discount_factor * next_q_value - self.q)

    def evaluate(self):
        return self.q

    def get_gym_action(self):
        return self.gym_value
