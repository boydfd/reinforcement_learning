from mdp.state import State


class Capital(State):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def __str__(self):
        return '{}:{}->{}'.format(self.count, list(self.current_policy.keys()), self.value)


class FinalCapital(State):
    def __init__(self):
        super().__init__()
        self.count = 100
        self.value = 1

    def evaluate(self):
        self.next_value = 1
        # return 100
