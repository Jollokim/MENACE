class AIPlayer:
    def __init__(self, board):
        self.board = board
        self.opponent = None
        self.data_boards = self.read_data()

    def create_all_boards(self):
        pass


    def get_an_opponent(self, oppenent):
        self.opponent

    def has_opponent(self):
        if self.opponent != None:
            print("Needs opponent!")
            return False
        return True

    def read_data(self):
        databoards = []

        with open("data.csv", "r") as data:
            for line in data:
                boarddata = line.split(",")

                for i in range(9):
                    databoards.append(boarddata)

        return databoards


    def write_data(self):
        pass

    def is_new_board(self):
        pass

    def play_move(self):
        pass

