from mdp.policy_iterator.iterator import Iterator


class PolicyIterator(Iterator):

    def policy_evaluate(self, max_delta=0.0001):
        while True:
            delta = self.evaluator.evaluate()
            self.printer.print_per_policy_evaluate()
            if delta < max_delta:
                break

    def _iterate(self):
        while True:
            self.policy_evaluate()
            stable = self.policy_improve()
            self.printer.print_per_policy_iterate()
            print('policy improve')
            if stable:
                self.printer.final_print()
                break

