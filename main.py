from game.game import Game


game = Game()
while True:
    game.playGame()
    print()
    while True:
        playAgain = input("Play again? (Y,N)")
        if playAgain.upper() not in ('Y', 'N'):
            print()
            print("Invalid input")
        else:
            break
    if playAgain == "N":
        break
    else:
        game.reset()
