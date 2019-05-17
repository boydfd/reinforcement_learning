# from unittest import TestCase
from pprint import pprint
from gridworld.builder import GridWorldBuilder
import unittest


class TestGridWorldBuilder(unittest.TestCase):
    def test_paddedWith_4x4_6x6Returned(self):
        gridWorld = [[0, -1, -1, -1, ],
                     [1, -1, -1, -1, ],
                     [1, -1, -1, -1, ],
                     [1, -1, -1, 0, ], ]
        self.assertEqual([
            [-1, -1, -1, -1, -1, -1, ],
            [-1, 0, -1, -1, -1, -1, ],
            [-1, 1, -1, -1, -1, -1, ],
            [-1, 1, -1, -1, -1, -1, ],
            [-1, 1, -1, -1, 0, -1, ],
            [-1, -1, -1, -1, -1, -1, ],
        ], GridWorldBuilder.pad_with(gridWorld, lambda: -1, (4, 4)))

    def test_improve_policy(self):

        builder = GridWorldBuilder(4, 4)
        builder.policy_iterate()

        cells = builder.foreacher.stats
        for i in range(len(cells)):
            print(*cells[i])

        self.assertEqual(['right'], cells[4][3].action_names())
        self.assertEqual(['right'], cells[4][2].action_names())
        self.assertEqual(['left', 'down'], cells[1][4].action_names())
