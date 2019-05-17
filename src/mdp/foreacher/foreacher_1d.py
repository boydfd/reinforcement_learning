from mdp.foreacher.foreacher import Foreacher


class Foreacher1D(Foreacher):
    def __init__(self, stats, length):
        super().__init__(stats)
        self.length = length

    def foreach(self, func):
        for i in range(self.length):
            func(self.stats[i])

    def foreach_return(self, func):
        for i in range(self.length):
            result = func(self.stats[i])
            yield result
