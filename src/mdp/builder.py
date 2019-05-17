from .policy_iterator.policy_iterator import PolicyIterator
import time


class Builder:
    def __init__(self, policy_iterator=None):
        if not policy_iterator:
            policy_iterator = PolicyIterator
        self.policy_iterator = policy_iterator(self)

    def iterate(self):
        self._foreach(lambda cell: cell.evaluate())
        max_delta = sum(list(self._foreach_return(lambda cell: cell.delta())))
        self._foreach(lambda cell: cell.replace_old_value())
        print(max_delta)
        return abs(max_delta)

    def policy_improve(self):
        self._foreach(lambda cell: cell.policy_improve())
        foreach_return = list(self._foreach_return(lambda cell: cell.update_policy()))
        return False not in foreach_return

    def _foreach(self, func):
        pass

    def _foreach_return(self, func):
        return []

    def policy_iterate(self):
        start = time.time()
        self.policy_iterator.iterate()
        end = time. time()
        print("time cost: {}".format(end - start))

    def print_per_policy_evaluate(self):
        pass

    def print_per_policy_iterate(self):
        pass

    def final_print(self):
        pass
