class Board:
    def __init__(self):
        self.spots = []
        for row in range(3):
            self.spots.append([])
            for col in range(3):
                self.spots[row].append("")

    def __str__(self):
        return self.spots

    def generate_all_moves(self):
        pass
