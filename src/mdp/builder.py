import time

from mdp.policy_iterator.policy_iterator import PolicyIterator


class Builder:
    def __init__(self, policy_iterator: PolicyIterator):
        self.policy_iterator = policy_iterator

    # def iterate(self):
    #     self._foreach(lambda stat: stat.evaluate())
    #     max_delta = sum(list(self._foreach_return(lambda stat: stat.delta())))
    #     self._foreach(lambda stat: stat.replace_old_value())
    #     print(max_delta)
    #     return abs(max_delta)

    # def iterate(self):
    #     max_delta = sum(list(self._foreach_return(lambda stat: stat.evaluate_inplace())))
    #     print(max_delta)
    #     return abs(max_delta)

    # def policy_improve(self):
    #     self._foreach(lambda stat: stat.policy_improve())
    #     policy_updated = list(self._foreach_return(lambda stat: stat.update_policy()))
    #     return False not in policy_updated

    # def _foreach(self, func):
    #     self.foreacher.foreach(func)
    #
    # def _foreach_return(self, func):
    #     return self.foreacher.foreach_return(func)

    def policy_iterate(self):
        start = time.time()
        self.policy_iterator.iterate()
        end = time.time()
        print("time cost: {}".format(end - start))

    def print_per_policy_evaluate(self):
        pass

    def print_per_policy_iterate(self):
        pass

    def final_print(self):
        pass
