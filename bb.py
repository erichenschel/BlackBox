import numpy as np
import random
from surr import surroundings

class Game:
    def __init__(self):
        self.boardSize = 8
        self.numAtoms = 4
        random.seed(6)

        
    # m x n matrix w/ rows=m, cols=n
    def blankBoard(self):
        return np.zeros((8, 8)).tolist()

    def placeAtom(self):
        row = random.randint(0, self.boardSize-1)
        col = random.randint(0, self.boardSize-1)
        return row, col

    def gameBoard(self):
        b = self.blankBoard()
        # place first atom
        atoms = [self.placeAtom()]
        # populate atoms array with numAtoms
        while len(atoms) < self.numAtoms:
            # place next atom
            atom = self.placeAtom()
            row, col = atom[0], atom[1]
            # check that distance between new atom and existing atoms is at least 1 due to force fields
            if len(atoms) >= 1:
                for a in atoms:
                    if row - a[0] > 1 and col - a[1] > 1:
                        pass
                    else:
                        break
                atoms.append(atom)

        for a in atoms:
            row=a[0]
            col=a[1]
            b[row][col] = 2.0

        board = np.array(b)
        
        return board, atoms

    # have user choose at which (row, col) to shoot a ray
    def rayStart(self):
        col = None
        row = None

        c1 = None
        pos = None

        while c1 == None:
            c1 = input("Select a firing position (top, bottom, right, left): ")
            # top - row == 0
            if c1 == 'top':
                row = 0
            # bottom - row == 7
            elif c1 == 'bottom':
                row = 7
            # right - col == 7
            elif c1 == 'right':
                col = 7
            # left - col == 0
            elif c1 == 'left':
                col = 0
            else:
                c1 = None
                print("Error: Invalid entry.")

        while pos == None:
            pos = input("Choose your position (0 - 7): ")
            if pos.isdigit():
                pos = int(pos)
                if pos < self.boardSize and col != None:
                    return pos, col
                elif pos < self.boardSize and row != None:
                    return row, pos
                else:
                    pos = None
                    print("Error: Invalid entry.")
            else:
                pos = None
                print("Error: Invalid entry.")


    def initDirection(self, start):
        if start[0] == 0:
            return 'Down'
        elif start[0] == self.boardSize-1:
            return 'Up'
        elif start[1] == 0:
            return 'Right'
        elif start[1] == self.boardSize-1:
            return 'Left'




if __name__=="__main__":
    G = Game()
    board = G.gameBoard()[0]
    print(board)
    start = G.rayStart()
    print('start', start)
    #d = G.initDirection(start)
    for i in range(8):
        for j in range(8):
            print((i, j))
            surr = surroundings((i, j), board)
            print(surr)
