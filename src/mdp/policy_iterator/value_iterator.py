from mdp.policy_iterator.iterator import Iterator


class ValueIterator(Iterator):
    def policy_evaluate(self, max_delta=0.0001):
        delta = 0
        for i in range(20):
            delta = self.evaluator.evaluate()
            self.printer.print_per_policy_evaluate()
        return delta < max_delta

    def _iterate(self):
        while True:
            value_stable = self.policy_evaluate()
            stable = self.policy_improve()
            print('policy improve')
            if stable and value_stable:
                self.printer.print_per_policy_iterate()
                break
