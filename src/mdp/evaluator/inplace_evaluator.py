from mdp.evaluator.evaluator import Evaluator


class InplaceEvaluator(Evaluator):
    def evaluate(self):
        max_delta = sum(list(self._foreach_return(lambda stat: stat.evaluate_inplace())))
        print(max_delta)
        return abs(max_delta)
