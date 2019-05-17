class PolicyIterator:
    def __init__(self, builder):
        self.builder = builder

    def policy_evaluate(self, max_delta=0.0001):
        for _ in range(10000000):
            delta = self.builder.iterate()
            self.builder.print_per_policy_evaluate()
            if delta < max_delta:
                break

    def iterate(self):
        while True:
            self.policy_evaluate()
            stable = self.builder.policy_improve()
            self.builder.print_per_policy_iterate()
            print('policy improve')
            if stable:
                self.builder.final_print()
                break
