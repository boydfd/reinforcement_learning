from mdp.builder import Builder
from mdp.foreacher.foreacher_1d import Foreacher1D


class CapitalBuilder(Builder):
    def __init__(self, stats, policy_iterator=None, max_count=101):
        super().__init__(Foreacher1D(stats, max_count), policy_iterator)

    def final_print(self):
        self._foreach(lambda stat: print(stat))
