from .iterator.policy_iterator import PolicyIterator
import time


class Builder:
    def __init__(self, iterator=None):
        if not iterator:
            iterator = PolicyIterator
        self.iterator = iterator(self)

    def iterate(self):
        self._foreach(lambda cell: cell.evaluate())
        max_delta = sum(list(self._foreach_return(lambda cell: cell.delta())))
        self._foreach(lambda cell: cell.replace_old_value())
        print(max_delta)
        return abs(max_delta)

    def improve(self):
        self._foreach(lambda cell: cell.policy_improve())
        foreach_return = list(self._foreach_return(lambda cell: cell.update_policy()))
        return False not in foreach_return

    def _foreach(self, func):
        pass

    def _foreach_return(self, func):
        return []

    def policy_iterate(self):
        start = time.time()
        self.iterator.iterate()
        end = time. time()
        print(end - start)

    def print_value_iterate(self):
        pass

    def print_policy(self):
        pass

    def print(self):
        pass
