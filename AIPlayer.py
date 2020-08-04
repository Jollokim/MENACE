class AIPlayer:
    def __init__(self, board):
        self.board = board
        self.opponent = None
        self.dataBoards = self.

    def create_all_boards(self):
        pass


    def getAnOpponent(self, oppenent):
        self.opponent

    def hasOpponent(self):
        if self.opponent != None:
            print("Needs opponent!")
            return False
        return True

    def readData(self):
        databoards = []

        with open("data.csv", "r") as data:
            for line in data:
                boarddata = line.split(",")

                for i in range(9):
                    databoards.append(boarddata)

        return databoards


    def writeData(self):
        pass

    def isNewBoard(self):
        pass

    def playMove(self):
        pass

