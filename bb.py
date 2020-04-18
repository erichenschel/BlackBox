import numpy as np
import random


class Game:
    def __init__(self):
        self.boardSize = 8
        self.numAtoms = 4
        #random.seed(6)

        
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

        board = np.array(b)
        
        return board, atoms



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

    def surrVals(self, currPos, board):
        row = currPos[0]
        col = currPos[1]

        # condition 1: row not in (0,7) and col not in (0, 7) ------------------------------------
        if row not in (0, self.boardSize-1) and col not in (0, self.boardSize-1):
            # indices surrounding currPos [up, down, left, right]
            I = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            # indices [up-left, up-right, down-left, down-right]
            II = [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]

        # condition 2: row in (0, 7) col not in (0, 7) -------------------------------------------
        if row == 0:
            # indices surrounding currPos [(up), down, left, right]
            I = [None, (row+1, col), (row, col-1), (row, col+1)]
            # indices [(up-left), (up-right), down-left, down-right]
            II = [None, None, (row+1, col-1), (row+1, col+1)]
        elif row == self.boardSize-1:
            # indices surrounding currPos [up, (down), left, right]
            I = [(row-1, col), None, (row, col-1), (row, col+1)]
            # indices [up-left, up-right, (down-left), (down-right)]
            II = [(row-1, col-1), (row-1, col+1), None, None]

        # condition 3: row not in (0, 7) col in (0, 7) -------------------------------------------
        if col == 0:
            # indices surrounding currPos [up, down, (left), right]
            I = [(row-1, col), (row+1, col), None, (row, col+1)]
            # indices [(up-left), up-right, (down-left), down-right]
            II = [None, (row-1, col+1), None, (row+1, col+1)]
        elif col == self.boardSize-1:
            # indices surrounding currPos [up, down, left, (right)]
            I = [(row-1, col), (row+1, col), (row, col-1), None]
            # indices [up-left, (up-right), down-left, (down-right)]
            II = [(row-1, col-1), None, (row+1, col-1), None]
        
        # condition 4: row in (0, 7) col in (0, 7) ---------------------------------------------
        if row == 0 and col == 0:
            # indices surrounding currPos [(up), down, (left), right]
            I = [None, (row+1, col), None, (row, col+1)]
            # indices [(up-left), (up-right), (down-left), down-right]
            II = [None, None, None, (row+1, col+1)]
        elif row == self.boardSize-1 and col == 0:
            # indices surrounding currPos [up, (down), (left), right]
            I = [(row-1, col), None, None, (row, col+1)]
            # indices [(up-left), up-right, (down-left), (down-right)]
            II = [None, (row-1, col+1), None, None]
        elif row == 0 and col == self.boardSize-1:
            # indices surrounding currPos [(up), down, left, (right)]
            I = [None, (row+1, col), (row, col-1), None]
            # indices [(up-left), (up-right), down-left, (down-right)]
            II = [None, None, (row+1, col-1), None]
        elif row == self.boardSize-1 and col == self.boardSize-1:
            # indices surrounding currPos [(up), down, (left), right]
            I = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            # indices [(up-left), (up-right), (down-left), down-right]
            II = [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]

        
        arr = []
        surr = []

        for i in range(I):
            if I[i] == None:
                val = 5
                arr.append(val)
            else:
                arr.append(val)
            
        # values surrounding currPos
        surr = [[board[II[0][0]][II[0][1]], board[I[0][0]][I[0][1]], board[II[1][0]][II[1][1]]],
                [board[I[2][0]][I[2][1]], board[row][col], board[I[3][0]][I[3][1]]],
                [board[II[2][0]][II[2][1]], board[I[1][0]][I[1][1]], board[II[3][0]][II[3][1]]]
                ]

        return surr



if __name__=="__main__":
    G = Game()
    board = G.gameBoard()
    ray = G.rayLocation()
    #path = G.rayPath(ray, board)
    surr = G.surrVals(ray, board)
    print(board)
    print(ray)
    #print(path)
    print(surr)
