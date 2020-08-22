
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

    def move(self, move, piece):
        try:
            row, col = move.split(" ")
        except ValueError:
            return {"success": False, "error": "Invalid input move must be in format: row col\nex: 2 2"}

        try:
            row = int(row)
            col = int(col)
            if row > 3 or col > 3 or row < 1 or col < 1:
                return {"success": False, "error": "Invalid input 1 <= row, col <= 3"}
        except ValueError:
            return {"success": False, "error": "Invalid input row and col must be integers"}

        if self.board[row-1][col-1] == None:
            self.board[row-1][col-1] = piece
            return {"success": True}
        else:
            return {"success": False, "error": "Invalid input cell not empty"}

    def resetBoard(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]