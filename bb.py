import numpy as np
import random


class Game:
    def __init__(self):
        self.boardSize = 8
        self.numAtoms = 4
        #random.seed(4)

        
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

            if row not in (0, self.boardSize-1):
                b[row-1][col] = 1.0
                b[row+1][col] = 1.0
            
            if col not in (0, self.boardSize-1):
                b[row][col-1] = 1.0
                b[row][col+1] = 1.0
             
            if col not in (0, self.boardSize-1) and row not in (0, self.boardSize-1):
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0

            if col == 0 and row not in (0, self.boardSize-1):
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row][col+1] = 1.0

            if col == self.boardSize-1 and row not in (0, self.boardSize-1):
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0
                b[row][col-1] = 1.0
            
            if col == 0 and row == 0:
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row][col+1] = 1.0

            if col == self.boardSize-1 and row == 0:
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0
                b[row][col-1] = 1.0
            
            if col == 0 and row == self.boardSize-1:
                b[row+1][col+1] = 1.0
                b[row-1][col+1] = 1.0
                b[row][col+1] = 1.0

            if col == self.boardSize-1 and row == self.boardSize-1:
                b[row+1][col-1] = 1.0
                b[row-1][col-1] = 1.0
                b[row][col-1] = 1.0

            if row == 0 and col not in (0, self.boardSize-1): 
                b[row+1][col+1] = 1.0
                b[row+1][col-1] = 1.0
                b[row+1][col] = 1.0

            if row == self.boardSize-1 and col not in (0, self.boardSize-1):
                b[row-1][col+1] = 1.0
                b[row-1][col-1] = 1.0
                b[row-1][col] = 1.0
                
       
            b[row][col] = 2.0
        
        return np.array(b), atoms





    # have user choose at which (row, col) to shoot a ray
    def rayEntry(self):
        while True:
            row = int(input("Select a row: "))
            col = int(input("Select a col: "))
            if row < self.boardSize-1 and col < self.boardSize-1:
                return row, col
            else:
                print("Error: Invalid entry.")
                print("Please select an integer between 0 and ", self.boardSize-1)

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
            #if self.rayEntry()[0] !=
            return True

        # detour
        def detour():

            return True
    



if __name__=="__main__":
    G = Game()
    board = G.gameBoard()
    ray = G.rayEntry()
    print(board)
    print(ray)
