import numpy as np

class Board:
    
    def __init__(self):
        self.playerTurn = 0
        self.grid = np.zeros((3, 3), dtype=int)
