class ValueIterator:
    def __init__(self, builder):
        self.builder = builder

    def value_iterate(self, max_delta=0.0001):
        delta = self.builder.iterate()
        self.builder.print_value_iterate()
        return delta < max_delta

    def iterate(self):
        while True:
            value_stable = self.value_iterate()
            stable = self.builder.improve()
            print('policy improve')
            if stable and value_stable:
                self.builder.print_policy()
                break
