from gridworld.action import create_normal_action
from gridworld.cell import EndCell, Cell


class GridWorldBuilder:
    def __init__(self, column_length, row_length):
        self.row_length = row_length
        self.column_length = column_length
        self.cells = None

    def build(self):
        column_length = self.column_length
        row_length = self.row_length

        cells = [[Cell(name='{}{}'.format(i, j)) for j in range(column_length)] for i in range(row_length)]

        cells = self.pad_with(cells, lambda: EndCell(), (row_length, column_length))
        cells[1][1] = EndCell()
        cells[row_length][column_length] = EndCell()
        # up
        for i in range(2, row_length + 1):
            for j in range(1, column_length + 1):
                cells[i][j].add_action(create_normal_action(cells[i - 1][j], 'up'))

        # left
        for i in range(1, row_length + 1):
            for j in range(2, column_length + 1):
                cells[i][j].add_action(create_normal_action(cells[i][j - 1], 'left'))

        # down
        for i in range(1, row_length):
            for j in range(1, column_length + 1):
                cells[i][j].add_action(create_normal_action(cells[i + 1][j], 'down'))

        # right
        for i in range(1, row_length + 1):
            for j in range(1, column_length):
                cells[i][j].add_action(create_normal_action(cells[i][j + 1], 'right'))

        self.cells = cells

    @classmethod
    def pad_with(cls, to_pad, initial_value_generator, shape):
        _, column = shape
        padded_row = [initial_value_generator()] * (column + 2)

        def pad_column(column):
            return [initial_value_generator()] + column + [initial_value_generator()]

        padded = list(map(pad_column, to_pad))
        return [padded_row] + padded + [padded_row]

    def iterate(self):
        self._foreach(lambda cell: cell.evaluate())
        max_delta = max(list(self._foreach_return(lambda cell: cell.delta())))
        self._foreach(lambda cell: cell.replace_old_value())
        return max_delta

    def improve(self):
        self._foreach(lambda cell: cell.policy_improve())
        foreach_return = list(self._foreach_return(lambda cell: cell.update_policy()))
        return False not in foreach_return

    def _foreach(self, func):
        for i in range(1, self.row_length + 1):
            for j in range(1, self.column_length + 1):
                func(self.cells[i][j])

    def _foreach_return(self, func):
        for i in range(1, self.row_length + 1):
            for j in range(1, self.column_length + 1):
                result = func(self.cells[i][j])
                if not ((i == 1 and j == 1) or (i == self.row_length and j == self.column_length)):
                    yield result

