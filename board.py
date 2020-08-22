
class Board():
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.remainingSlots = 9

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
            self.remainingSlots -= 1
            return {"success": True}
        else:
            return {"success": False, "error": "Invalid input cell not empty"}

    def checkGameState(self, piece):
        pieceIndexList = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == piece:
                    pieceIndexList.append([row, col])

        # check for winning configurations
        if all(elem in pieceIndexList for elem in [[0, 0], [0, 1], [0, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[1, 0], [1, 1], [1, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[2, 0], [2, 1], [2, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[0, 0], [1, 0], [2, 0]]):
            return piece
        if all(elem in pieceIndexList for elem in [[1, 0], [1, 1], [1, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[2, 0], [2, 1], [2, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[0, 0], [1, 1], [2, 2]]):
            return piece
        if all(elem in pieceIndexList for elem in [[0, 2], [1, 1], [2, 0]]):
            return piece
        else:
            return None

    def resetBoard(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.remainingSlots = 9
