import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board(self):
        initialBoard = [[None for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.board.board, initialBoard)

    def test_move(self):
        # Valid Move
        moveRes = self.board.move("1 1", 'X')
        newBoard = [[None for _ in range(3)] for _ in range(3)]
        newBoard[0][0] = 'X'
        self.assertEqual(moveRes, {"success": True})
        self.assertEqual(self.board.board, newBoard)

        # Invalid Moves
        # Incorrect format
        self.board.resetBoard()
        initialBoard = [[None for _ in range(3)] for _ in range(3)]
        moveRes = self.board.move("11", 'X')
        self.assertEqual(moveRes, {
                         "success": False, "error": "Invalid input move must be in format: row col\nex: 2 2"})
        self.assertEqual(self.board.board, initialBoard)

        # Non integers used
        moveRes = self.board.move("a b", 'X')
        self.assertEqual(moveRes, {
                         "success": False, "error": "Invalid input row and col must be integers"})
        self.assertEqual(self.board.board, initialBoard)

        # Out of range
        moveRes = self.board.move("4 5", 'X')
        self.assertEqual(
            moveRes, {"success": False, "error": "Invalid input 1 <= row, col <= 3"})
        self.assertEqual(self.board.board, initialBoard)

        moveRes = self.board.move("0 0", 'X')
        self.assertEqual(
            moveRes, {"success": False, "error": "Invalid input 1 <= row, col <= 3"})
        self.assertEqual(self.board.board, initialBoard)

        # Cell not empty
        self.board.move("1 1", "X")
        moveRes = self.board.move("1 1", 'X')
        initialBoard[0][0] = 'X'
        self.assertEqual(
            moveRes, {"success": False, "error": "Invalid input cell not empty"})
        self.assertEqual(self.board.board, initialBoard)


if __name__ == "__main__":
    unittest.main()
