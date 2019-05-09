
class Action:
    def __init__(self, immediate_reward, action_state, name=None, discount_rate=1):
        self.immediate_reward = immediate_reward
        self.action_state = action_state
        self.name = name
        self.discount_rate = discount_rate
        self.action = None

    def evaluate(self):
        return self.immediate_reward + self.discount_rate * self.action_state.evaluate()

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.__str__()

