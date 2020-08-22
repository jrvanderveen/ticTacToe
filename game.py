from board import Board
from player import Player


class Game():
    def __init__(self):
        self.board = Board()
        self.playerOne = Player('X')
        self.playerTwo = Player('O')

    def playGame(self):
        print("Welcome! Here is your board:\n")
        self.board.printBoard()
