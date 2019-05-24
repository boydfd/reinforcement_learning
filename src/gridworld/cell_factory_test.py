import unittest

from .cell_factory import CellFactory


class CellFactoryTest(unittest.TestCase):
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
        ], CellFactory.pad_with(gridWorld, lambda: -1, (4, 4)))
