from board import Board
from player import Player


class Game():
    def __init__(self):
        self.board = Board()
        self.playerOne = Player('Player1', 'X')
        self.playerTwo = Player('Player2', 'O')
        self.winner = None
        self.remainingSlots = 9
        self.currentPlayer = self.playerOne

    def playGame(self):
        print("Welcome! Here is your board:", end="\n\n")
        self.board.printBoard()

        while self.winner == None and self.remainingSlots > 0:
            self.turn()
            self.board.printBoard()
            self.currentPlayer = self.playerOne if self.currentPlayer == self.playerTwo else self.playerTwo

    def turn(self):
        while True:
            print()
            print(
                f'{self.currentPlayer.name} ({self.currentPlayer.piece}) where would you like to move?', end="\n\n")
            move = input()
            moveResult = self.board.move(move, self.currentPlayer.piece)
            if moveResult["success"] == False:
                print()
                print(moveResult["error"])
            else:
                print()
                break
