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

    def surroundings(self, currPos):
        board = self.gameBoard()[0]
        row = currPos[0]
        col = currPos[1]

        # condition 1: row not in (0,7) and col not in (0, 7) ------------------------------------
        if row not in (0, self.boardSize-1) and col not in (0, self.boardSize-1):
            # indices [up-right, up, up-left]
            I = [(row-1, col-1), (row-1, col), (row-1, col+1)]
            # indices [left, right]
            II = [(row, col-1), 1, (row, col+1)]
            # indices [down-left, down, down-right]
            III = [(row+1, col-1), (row+1, col), (row+1, col+1)]


































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

        # create matrix of surroundings for currPos
        for i in range(len(I)):
            idx = I[i]
            if idx != None:
                val = board[idk[0]][idk[1]]
                arr.append(val)
            else:
                arr.append(5)




        # values surrounding currPos
        surr = [[board[II[0][0]][II[0][1]], board[I[0][0]][I[0][1]], board[II[1][0]][II[1][1]]],
                [board[I[2][0]][I[2][1]], board[row][col], board[I[3][0]][I[3][1]]],
                [board[II[2][0]][II[2][1]], board[I[1][0]][I[1][1]], board[II[3][0]][II[3][1]]]
                ]

        return surr




if __name__=="__main__":
    G = Game()
    board = G.gameBoard()
    start = G.rayStart()
    d = G.initDirection(start)
    print(board)
    print(start)
    print(d)
