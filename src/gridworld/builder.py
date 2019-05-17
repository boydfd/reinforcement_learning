from gridworld.action import create_normal_action
from gridworld.cell import EndCell, Cell
from mdp.builder import Builder
from mdp.foreacher.foreacher_2d_padded import Foreacher2DPadded


class GridWorldBuilder(Builder):
    def __init__(self, column_length, row_length):
        super().__init__(Foreacher2DPadded(self.build_cells(column_length, row_length), row_length, column_length))

    def build_cells(self, column_length, row_length):
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

        return cells

    @classmethod
    def pad_with(cls, to_pad, initial_value_generator, shape):
        _, column = shape
        padded_row = [initial_value_generator()] * (column + 2)

        def pad_column(column):
            return [initial_value_generator()] + column + [initial_value_generator()]

        padded = list(map(pad_column, to_pad))
        return [padded_row] + padded + [padded_row]

