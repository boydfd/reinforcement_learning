from mdp.foreacher.foreacher import Foreacher
from mdp.printer.printer import Printer


class ForeachPrinter(Printer):
    def __init__(self, stats, foreacher: Foreacher):
        super().__init__(stats)
        self.foreacher = foreacher

    def final_print(self):
        self.foreacher.foreach(lambda stat: print(stat))

