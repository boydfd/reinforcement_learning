
class Action:
    def __init__(self, immediate_reward, action_states, name=None):
        self.immediate_reward = immediate_reward
        self.action_states = action_states
        self.name = name

    def evaluate(self):
        return self.immediate_reward + self.action_states.evaluate()

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.__str__()

