import time

from mdp.evaluator.evaluator import Evaluator
from mdp.evaluator.full_sweep_evaluator import FullSweepEvaluator
from mdp.foreacher.foreacher import Foreacher


class Iterator:
    def __init__(self, foreacher: Foreacher, printer, evaluator: Evaluator = None):
        self.foreacher = foreacher
        if not evaluator:
            evaluator = FullSweepEvaluator(foreacher)
        self.evaluator = evaluator
        self.printer = printer

    def _iterate(self):
        pass

    def policy_improve(self):
        self._foreach(lambda stat: stat.policy_improve())
        policy_updated = list(self._foreach_return(lambda stat: stat.update_policy()))
        return False not in policy_updated

    def iterate(self):
        start = time.time()
        self._iterate()
        end = time.time()
        print("time cost: {}".format(end - start))

    def _foreach(self, func):
        self.foreacher.foreach(func)

    def _foreach_return(self, func):
        return self.foreacher.foreach_return(func)
