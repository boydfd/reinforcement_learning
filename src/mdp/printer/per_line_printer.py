from mdp.printer.printer import Printer


class PerLinePrinter(Printer):
    def __init__(self, stats):
        super().__init__(stats)

    def final_print(self):
        self.print_per_line()

    def print_per_line(self):
        for i in range(len(self.stats)):
            print(*self.stats[i])
