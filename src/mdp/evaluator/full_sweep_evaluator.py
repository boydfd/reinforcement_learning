from mdp.evaluator.evaluator import Evaluator


class FullSweepEvaluator(Evaluator):
    def evaluate(self):
        self._foreach(lambda stat: stat.evaluate())
        max_delta = sum(list(self._foreach_return(lambda stat: stat.delta())))
        self._foreach(lambda stat: stat.replace_old_value())
        print(max_delta)
        return abs(max_delta)
