import numpy as np

from matchbox import Matchbox


class Ai:
    def __init__(self) -> None:
        self.matchboxlist = []
        for i in range(9):
            self.matchboxlist.append([])


    def generate_all_matchboxes(self):

        signature = np.zeros((3, 3), dtype=int)

        matchbox = Matchbox(signature, 0)

        self.matchboxlist[0].append(matchbox)


        for turn in range(1, len(self.matchboxlist)):
            for matchbox in self.matchboxlist[turn - 1]:
                
                
                for row in range(3):
                    for col in range(3):
                        signature = matchbox.signature.copy()
                        if signature[row, col] != 0:
                            continue

                        # set o
                        if (turn % 2) == 1:
                            signature[row, col] = 1
                        # set x
                        else:
                            signature[row, col] = 2

                        if self.has_reflection(signature, turn) or self.has_rotation(signature, turn):
                            continue
                        
                        self.matchboxlist[turn].append(Matchbox(signature, turn))
            print(f"Calculated turn {turn}, length: {len(self.matchboxlist[turn])}")
            

        print("Writing combs")
        self.write_combinations()
        print("Finished")


    def write_combinations(self):
        with open("combinations.csv", "w") as f:
            for l in self.matchboxlist:
                for box in l:
                    for row in range(len(box.signature)):
                        for col in range(len(box.signature)):
                            if row == len(box.signature)-1 and col == len(box.signature)-1:
                                f.write('\n')
                                continue
                            f.write(f"{box.signature[row, col]},")

                    
                


    def has_reflection(self, signature, turn) -> bool:
        knownBoxes = self.matchboxlist[turn]

        for box in knownBoxes:
            knownSign = box.signature

            if np.array_equal(knownSign, np.flip(signature, 0)) or np.array_equal(knownSign, np.flip(signature, 1)):
                return True
        return False


    def has_rotation(self, signature, turn) -> bool:
        knownBoxes = self.matchboxlist[turn]

        for box in knownBoxes:
            knownSign = box.signature

            # SJEKK HER
            if np.array_equal(knownSign, np.rot90(signature, 1)) or np.array_equal(knownSign, np.rot90(signature, 2)) or np.array_equal(knownSign, np.rot90(signature, 3)):
                return True
        return False