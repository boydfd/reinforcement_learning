from mdp.action.first_mc_action import FirstMCAction


class HitAction(FirstMCAction):
    def __init__(self, epsilon=None):
        super().__init__(self.epsilon, 'hit')

    @staticmethod
    def is_stick():
        return False

    def get_result(self):
        return 1


class StickAction(FirstMCAction):
    def __init__(self, epsilon=None):
        super().__init__(self.epsilon, 'stick')

    @staticmethod
    def is_stick():
        return True

    def get_result(self):
        return 0
