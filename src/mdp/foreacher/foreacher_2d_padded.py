from mdp.foreacher.foreacher import Foreacher


class Foreacher2DPadded(Foreacher):
    def __init__(self, stats, row_length, column_length):
        super().__init__(stats)
        self.row_length = row_length
        self.column_length = column_length

    def foreach(self, func):
        for i in range(1, self.row_length + 1):
            for j in range(1, self.column_length + 1):
                func(self.stats[i][j])

    def foreach_return(self, func):
        for i in range(1, self.row_length + 1):
            for j in range(1, self.column_length + 1):
                result = func(self.stats[i][j])
                if not ((i == 1 and j == 1) or (i == self.row_length and j == self.column_length)):
                    yield result
