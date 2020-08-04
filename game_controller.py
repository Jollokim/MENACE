import random
class GameController:

    def start_game(player1, player2):
        randint = random.randint(0,1)
        print(randint)

        if randint == 0:
            player1.play_move()
        else:
            player2.play_move




