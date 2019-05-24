class Evaluator:
    def __init__(self, foreacher):
        self.foreacher = foreacher

    def evaluate(self):
        pass

    def _foreach(self, func):
        self.foreacher.foreach(func)

    def _foreach_return(self, func):
        return self.foreacher.foreach_return(func)
