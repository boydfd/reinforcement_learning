from mdp.builder import Builder


class CapitalBuilder(Builder):
    def __init__(self, stats, iterator=None, max_count=101):
        super().__init__(iterator)
        self.max_count = max_count
        self.stats = stats

    def _foreach(self, func):
        for i in range(self.max_count):
                func(self.stats[i])

    def _foreach_return(self, func):
        for i in range(self.max_count):
            result = func(self.stats[i])
            yield result

    def final_print(self):
        for i in range(len(self.stats)):
            print(self.stats[i])
