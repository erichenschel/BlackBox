import numpy as np
import random


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
        # place atoms
        atoms = []
        for i in range(self.numAtoms):
            atom = self.placeAtom()
            row, col = atom[0], atom[1]
            atoms.append(atom)
        
        # make force fields
        for a in atoms:
            row = a[0]
            col = a[1]
            
            # condition 1: row not in (0,7) and col not in (0, 7) ------------------------------------
            if row not in (0, self.boardSize-1):
                b[row+1][col] = 1.0
                b[row-1][col] = 1.0  
            if row not in (0, self.boardSize-1) and col not in (0, self.boardSize-1):
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0
            if col not in (0, self.boardSize-1):
                b[row][col+1] = 1.0
                b[row][col-1] = 1.0

            # condition 2: row in (0, 7) col not in (0, 7) -------------------------------------------
            if row == 0 and col not in (0, self.boardSize-1): 
                b[row+1][col+1] = 1.0
                b[row+1][col-1] = 1.0
                b[row+1][col] = 1.0
            if row == self.boardSize-1 and col not in (0, self.boardSize-1):
                b[row-1][col+1] = 1.0
                b[row-1][col-1] = 1.0
                b[row-1][col] = 1.0

            # condition 3: row not in (0, 7) col in (0, 7) -------------------------------------------
            if row not in (0, self.boardSize-1) and col == 0:
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row][col+1] = 1.0

            if row not in (0, self.boardSize-1) and col == self.boardSize-1:
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0
                b[row][col-1] = 1.0
                
            # condition 4: row in (0, 7) col in (0, 7) ---------------------------------------------
            if row == 0 and col == 0:
                b[row][col+1] = 1.0
                b[row+1][col+1] = 1.0
                b[row+1][col] = 1.0

            if row == self.boardSize-1 and col == 0:
                b[row][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row-1][col] = 1.0
            
            if row == 0 and col == self.boardSize-1:
                b[row][col-1] = 1.0
                b[row+1][col] = 1.0
                b[row+1][col-1] = 1.0
            
            if row == self.boardSize-1 and col == self.boardSize-1:
                b[row][col-1] = 1.0
                b[row-1][col-1] = 1.0
                b[row-1][col] = 1.0
                
        for a in atoms:
            print(a)
            row=a[0]
            col=a[1]
            b[row][col] = 2.0
        
        return np.array(b), atoms



    # have user choose at which (row, col) to shoot a ray
    def rayLocation(self):
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
            if pos == int(pos):
                pos = int(pos)
            
            if pos > self.boardSize-1:
                print("Error: Invalid entry.") 
            elif pos < self.boardSize and col != None:
                return pos, col
            elif pos < self.boardSize and row != None:
                return row, pos
            else:
                pos = None

    def rayExit(self):

        #return row, col
        return 0
    
    def interactions(self):
        # hit
        def hit():

            return True

        # deflection
        def deflection():

            return True

        # reflection
        def reflection():

            return True

        # double deflection
        def doubDeflection():

            return True

        # miss
        def miss():
            #for i in range(self.boardSize-1):

            return True

        # detour
        def detour():

            return True
    



if __name__=="__main__":
    G = Game()
    board = G.gameBoard()
    ray = G.rayLocation()
    print(board)
    print(ray)
