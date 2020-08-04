class Board:
    board_len = 9

    def __init__(self):
        self.generate_all_moves()



    def generate_all_moves(self):
        print("This will generate all possible moves, and boards")

        boards = [
            # board at start
            [
                ["", "", "", "", "", "", "", "", ""]
            ],
            # turn 1 moves
            [

            ]
        ]
        # print(boards[0] == boards[0])
        # print(boards[0])
        # print(boards[0][0])

        move_turn = 0
        done = False

        while not done:


            for moves in range(len(boards[move_turn])):


                for spot in range(len(boards[move_turn][moves])):

                    if boards[move_turn][moves][spot] == "":

                        new_move = boards[move_turn][moves]
                        # print(new_move)

                        if move_turn % 2 == 0:
                            new_move[spot] = "X"

                        else:
                            new_move[spot] = "O"

                        if self.test_unique(new_move, boards[move_turn + 1]):
                            print(new_move, "is unique")
                            pass
    #                     append move to list of moves in next turn
    # create new move list for second turn











    def test_unique(self, new_move, moves):
        for move in moves:
            # test reflections of new_move already exist
            if (
                self.create_horizontal_reflection(new_move) == move or
                self.create_vertical_reflection(new_move) == move
            ):
                return False

            rotated_new_move = self.create_rotation(new_move)

            # test rotation of new_move already exist
            for i in range(3):
                if rotated_new_move == move:
                    return False

                rotated_new_move = self.create_rotation(rotated_new_move)

            reflection = self.create_horizontal_reflection(new_move)
            rotated_reflection = self.create_rotation(reflection)

            # test rotation of reflection of new move exist
            for i in range(2):

                if rotated_reflection == move:
                    return False
                rotated_reflection = self.create_rotation(reflection, 0)

            return True






    def create_horizontal_reflection(self, board):
        pass

    def create_vertical_reflection(self, board):
        pass

    def create_rotation(self, board, *args):
        pass

    def row_complete(self, board):
        pass

    def __str__(self):
        return self.spots
