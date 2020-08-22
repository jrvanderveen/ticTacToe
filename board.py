
class Board():
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        for row in range(3):
            for col in range(3):
                print("_" if self.board[row][col] ==
                      None else self.board[row][col], end="")
                if col < 2:
                    print(" , ", end="")
            print()
