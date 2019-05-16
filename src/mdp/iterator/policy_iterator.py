class PolicyIterator:
    def __init__(self, builder):
        self.builder = builder

    def value_iterate(self, max_delta=0.0001):
        for _ in range(10000000):
            if self.builder.iterate() < max_delta:
                # self.builder.print_value_iterate()
                break
            # self.builder.print_value_iterate()

    def iterate(self):
        while True:
            self.value_iterate()
            stable = self.builder.improve()
            self.builder.print_policy()
            print('policy improve')
            if stable:
                self.builder.print_value_iterate()
                self.builder.print()
                break
