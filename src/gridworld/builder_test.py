# from unittest import TestCase
from pprint import pprint
from gridworld.builder import GridWorldBuilder
import unittest

from gridworld.cell_factory import CellFactory
from mdp.builder import Builder
from mdp.foreacher.foreacher_2d_padded import Foreacher2DPadded
from mdp.policy_iterator.policy_iterator import PolicyIterator
from mdp.printer.per_line_printer import PerLinePrinter


class TestGridWorldBuilder(unittest.TestCase):
    def test_improve_policy(self):

        row_length = 4
        column_length = 4
        cells = CellFactory(row_length, column_length).cells
        foreacher = Foreacher2DPadded(cells, row_length, column_length)
        printer = PerLinePrinter(cells)
        policy_iterator = PolicyIterator(foreacher, printer)
        policy_iterator.iterate()

        self.assertEqual(['right'], cells[4][3].action_names())
        self.assertEqual(['right'], cells[4][2].action_names())
        self.assertEqual(['left', 'down'], cells[1][4].action_names())
