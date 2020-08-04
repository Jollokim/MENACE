import random
class GameController:
    def startGame(player1, player2):
        randint = random.randint(0,1)
        print(randint)

        if randint == 0:
            player1.playMove()
        else:
            player2.playMove




