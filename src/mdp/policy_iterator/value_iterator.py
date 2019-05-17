class ValueIterator:
    def __init__(self, builder):
        self.builder = builder

    def policy_evaluate(self, max_delta=0.0001):
        delta = 0
        for i in range(20):
            delta = self.builder.iterate()
            self.builder.print_per_policy_evaluate()
        return delta < max_delta

    def iterate(self):
        while True:
            value_stable = self.policy_evaluate()
            stable = self.builder.policy_improve()
            print('policy improve')
            if stable and value_stable:
                self.builder.print_per_policy_iterate()
                break
