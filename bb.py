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



    def surroundings(self, currPos):
        board = self.gameBoard()[0]
        print(board)
        row = currPos[0]
        col = currPos[1]

        # condition 1: row not in (0,7) and col not in (0, 7) ------------------------------------
        if row not in (0, self.boardSize-1) and col not in (0, self.boardSize-1):
            # indices [up-left, up, up-right]
            I = [(row-1, col-1), (row-1, col), (row-1, col+1)]
            # indices [left, right]
            II = [(row, col-1), (row, col), (row, col+1)]
            # indices [down-left, down, down-right]
            III = [(row+1, col-1), (row+1, col), (row+1, col+1)]
            
            arr = [I, II, III]
            tmp = []
            surr = []
            for i in arr:
                for r, c in i:
                    if r == row and c == col:
                        tmp.append(7)
                    else:
                        v = board[r][c]
                        tmp.append(v)
                surr.append(tmp)
                tmp = []

            return np.array(surr)

        # condition 2: row in (0, 7) col not in (0, 7) -------------------------------------------
        if row == 0 and col not in (0, self.boardSize-1):
            # indices [left, mid, right]
            II = [(row, col-1), (row, col), (row, col+1)]
            # indices [down-left, down, down-right]
            III = [(row+1, col-1), (row+1, col), (row+1, col+1)]

            arr = [II, III]
            tmp = []
            surr = []
            for i in arr:
                for r, c in i:
                    if r == row and c == col:
                        tmp.append(7)
                    else:
                        v = board[r][c]
                        tmp.append(v)
                surr.append(tmp)
                tmp = []

            return np.array(surr)
        
        elif row == self.boardSize-1 and col not in (0, self.boardSize-1):
            # indices [up-left, up, up-right]
            I = [(row-1, col-1), (row-1, col), (row-1, col+1)]
            # indices [left, right]
            II = [(row, col-1), (row, col), (row, col+1)]

            arr = [I, II]
            tmp = []
            surr = []
            for i in arr:
                for r, c in i:
                    v = board[r][c]
                    if r == row and c == col and v != 2:
                        tmp.append(7)
                    else:
                        tmp.append(v)
                surr.append(tmp)
                tmp = []

            return np.array(surr)


        # condition 3: row not in (0, 7) col in (0, 7) -------------------------------------------
        if row not in (0, self.boardSize-1) and col == 0:
            # indices [None, up, up-right]
            I = [None, (row-1, col), (row-1, col+1)]
            # indices [None, mid, right]
            II = [None, (row, col), (row, col+1)]
            # indices [None, down, down-right]
            III = [None, (row+1, col), (row+1, col+1)]

            arr = [I, II, III]
            tmp = []
            surr = []
            for i in arr:
                for r, c in i:
                    v = board[r][c]
                        if r == row and c == col and v != 2:
                            tmp.append(7)
                        else:
                            tmp.append(v)
                    # off board val == 5
                    else:
                        tmp.append(5)
                surr.append(tmp)
                tmp = []

            return np.array(surr)

        elif row not in (0, self.boardSize) and col == self.boardSize-1:
            # indices [up-left, up, None]
            I = [(row-1, col-1), (row-1, col), None]
            # indices [left, mid, None]
            II = [(row, col-1), (row, col), None]
            # indices [down-left, down, None]
            III = [(row+1, col-1), (row+1, col), None]

            arr = [I, II, III]
            tmp = []
            surr = []
            for i in arr:
                for r, c in i:
                    v = board[r][c]
                    if v != None:
                        if r == row and c == col and v != 2:
                            tmp.append(7)
                        else:
                            tmp.append(v)
                    # off board val == 5
                    else:
                        tmp.append(5)
                surr.append(tmp)
                tmp = []

            return np.array(surr)
"""
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
"""



if __name__=="__main__":
    G = Game()
    #board = G.gameBoard()
    #print(board)
    start = G.rayStart()
    print('start', start)
    #d = G.initDirection(start)
    surr = G.surroundings((4, 0))
    print(surr)
