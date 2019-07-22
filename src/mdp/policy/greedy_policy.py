class GreedyPolicy:
    @classmethod
    def pick_action(cls, actions):
        max_action = None
        value = -9e9
        for action in actions:
            evaluate = action.q
            if evaluate > value:
                max_action = action
                value = evaluate
        return max_action
