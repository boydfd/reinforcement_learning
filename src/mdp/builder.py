class Builder:
    def _iterate(self):
        self._foreach(lambda cell: cell.evaluate())
        max_delta = max(list(self._foreach_return(lambda cell: cell.delta())))
        self._foreach(lambda cell: cell.replace_old_value())
        return max_delta

    def _improve(self):
        self._foreach(lambda cell: cell.policy_improve())
        foreach_return = list(self._foreach_return(lambda cell: cell.update_policy()))
        return False not in foreach_return

    def _foreach(self, func):
        pass

    def _foreach_return(self, func):
        return []

    def value_iterate(self, max_delta=0.000000001):
        for _ in range(10000000):
            if -self._iterate() < max_delta:
                self._print_value_iterate()
                break
            self._print_value_iterate()

    def policy_iterate(self):
        while True:
            self.value_iterate()
            if self._improve():
                self._print_policy()
                break
            self._print_policy()

    def _print_value_iterate(self):
        pass

    def _print_policy(self):
        pass
