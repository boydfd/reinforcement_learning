from mdp.foreacher.foreacher import Foreacher


class Foreacher2D(Foreacher):
    def __init__(self, stats, row_length, column_length):
        super().__init__(stats)
        self.row_length = row_length
        self.column_length = column_length

    def foreach(self, func):
        for i in range(self.row_length):
            for j in range(self.column_length):
                func(self.stats[i][j])

    def foreach_return(self, func):
        for i in range(self.row_length):
            for j in range(self.column_length):
                result = func(self.stats[i][j])
                yield result

