from typing import Dict


class Matchbox:
    def __init__(self, signature, turn) -> None:
        self.signature = signature # board state
        self.turn = turn
        self.gems = {} #index: number of gems

    def __str__(self) -> str:
        return self.signature

    

        
    