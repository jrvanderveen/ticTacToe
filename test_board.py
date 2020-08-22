import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board(self):
        initialBoard = [[None for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.board.board, initialBoard)


if __name__ == "__main__":
    unittest.main()
