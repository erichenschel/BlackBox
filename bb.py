import numpy as np
import random
from surr import surroundings as surr

class Game:
    def __init__(self):
        self.boardSize = 8
        self.numAtoms = 4
        random.seed(6)

        
    # m x n matrix w/ rows=m, cols=n
    def blankBoard(self):
        return np.zeros((8, 8)).tolist()

    # function to generate a random atom located on the grid
    def placeAtom(self):
        row = random.randint(0, self.boardSize-1)
        col = random.randint(0, self.boardSize-1)
        return row, col
    
    # have computer make a game board
    def gameBoard(self):
        b = self.blankBoard()
        # place first atom
        atoms = [self.placeAtom()]
        # populate atoms array with numAtoms
        while len(atoms) < self.numAtoms:
            # place next atom
            atom = self.placeAtom()
            row, col = atom[0], atom[1]

            # check that distance b/w atoms >= 1
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
            d = None
            # top - row == 0
            if c1 == 'top':
                row = 0
                d = 'down'
            # bottom - row == 7
            elif c1 == 'bottom':
                row = 7
                d = 'up'
            # right - col == 7
            elif c1 == 'right':
                col = 7
                d = 'left'
            # left - col == 0
            elif c1 == 'left':
                col = 0
                d = 'right'
            else:
                c1 = None
                print("Error: Invalid entry.")

        while pos == None:
            pos = input("Choose your position (0 - 7): ")
            if pos.isdigit():
                pos = int(pos)
                if pos < self.boardSize and col != None:
                    return (pos, col), d
                elif pos < self.boardSize and row != None:
                    return (row, pos), d
                else:
                    pos = None
                    print("Error: Invalid entry.")
            else:
                pos = None
                print("Error: Invalid entry.")

    # step functions that return nextPos of ray and direction
    def stepRight(self, currPos):
        row, col = currPos
        nextPos = (row, col+1)
        direction = 'right'
        return nextPos, direction
    def stepLeft(self, currPos):
        row, col = currPos
        direction = 'left'
        nextPos = (row, col-1)
        return nextPos, direction
    def stepUp(self, currPos):
        row, col = currPos
        direction = 'up'
        nextPos = (row-1, col)
        return nextPos, direction
    def stepDown(self, currPos):
        row, col = currPos
        direction = 'down'
        nextPos = (row+1, col)
        return nextPos, direction


    # check for initial edge node hits - cond 2
    def hasHitAtom(self, currPos, board):
        S = surr(currPos, board)
        if d == 'down' and S[2][1] == 2:
            return True
        elif d == 'down'and S[1][1] == 2:
            return True

        elif d == 'up' and S[0][1] == 2:
            return True
        elif d == 'up' and S[1][1] == 2:
            return True
        
        elif d == 'left' and S[1][0] == 2:
            return True
        elif d == 'left' and S[1][1] == 2:
            return True
        
        elif d == 'right' and S[1][2] == 2:
            return True
        elif d == 'right' and S[1][1] == 2:
            return True

        else:
            return False


    # check for right turn condition - cond 3
    def isRightTurn(self, currPos, board, d):
        if d == 'up' and surr(currPos, board)[0][0] == 2:
            return self.stepRight(currPos)
        elif d == 'down' and surr(currPos, board)[2][0] == 2:
            return self.stepRight(currPos)
        else:
            return False
    

    # check for left turn condition - cond 4
    def isLeftTurn(self, currPos, board, d):
        if d == 'up' and surr(currPos, board)[0][2] == 2:
            return self.stepLeft(currPos)
        elif d == 'down' and surr(currPos, board)[2][2] == 2:
            return self.stepLeft(currPos)
        else:
            return False
    
    
    # check for up turn condition - cond 5
    def isUpTurn(self, currPos, board, d):
        if d == 'right' and surr(currPos, board)[2][2] == 2:
            return self.stepUp(currPos)
        elif d == 'left' and surr(currPos, board)[2][0] == 2:
            return self.stepUp(currPos)
        else:
            return False


    # check for down turn condition - cond 6
    def isDownTurn(self, currPos, board, d):
        if d == 'right' and surr(currPos, board)[0][2] == 2:
            return self.stepDown(currPos)
        elif d == 'left' and surr(currPos, board)[0][0] == 2:
            return self.stepDown(currPos)
        else:
            return False
       

    # check for reflection - cond 6
    def isReflection(self, currPos, board, d):
        if d == 'up' and surr(currPos, board)[1][0] == 2 and surr(currPos, board)[2][1] == 5:
            return print('Reflection')
        elif d == 'up' and surr(currPos, board)[1][2] == 2 and surr(currPos, board)[2][1] == 5:
            return print('Reflection')


        elif d == 'down' and surr(currPos, board)[1][0] == 2 and surr(currPos, board)[0][1] == 5:
            return print('Reflection')
        elif d == 'down' and surr(currPos, board)[1][2] == 2 and surr(currPos, board)[0][1] == 5:
            return print('Reflection')


        elif d == 'right' and surr(currPos, board)[0][1] == 2 and surr(currPos, board)[1][0] == 5:
            return print('Reflection')
        elif d == 'right' and surr(currPos, board)[2][1] == 2 and surr(currPos, board)[1][0] == 5:
            return print('Reflection')


        elif d == 'left' and surr(currPos, board)[0][1] == 2 and surr(currPos, board)[1][0] == 5:
            return print('Reflection')
        elif d == 'left' and surr(currPos, board)[2][1] == 2 and surr(currPos, board)[1][0] == 5:
            return print('Reflection')
        




    # function which returns the path a ray 
    # takes from a starting place and initial
    # direction for a given board
    # empty path means node on edge of board at start
    def path(self, start, direction, board):
        d = direction
        path = []
        currPos = start
        exited = False

        while not exited:

            r, c = currPos
            if r < self.boardSize and c < self.boardSize and r >= 0 and c >=0:

                # check for initial edge node hits - cond 2
                if self.hasHitAtom(currPos, board):
                    exited = self.hasHitAtom(currPos, board)
                    path.append(('hit', currPos))
                    return path
                    
                path.append(currPos)

                # check for reflections from edge nodes - cond 7
                if self.isReflection(currPos, board, d):
                    return self.isReflection(currPos, board, d)


                # check for right turn condition - cond 3
                if self.isRightTurn(currPos, board, d) != False:
                    currPos, d = self.isRightTurn(currPos, board, d)
                    pass

                # check for left turn condition - cond 4
                elif self.isLeftTurn(currPos, board, d) != False:
                    currPos, d = self.isLeftTurn(currPos, board, d)
                    pass

                # check for up turn condition - cond 5
                elif self.isUpTurn(currPos, board, d) != False:
                    currPos, d = self.isUpTurn(currPos, board, d)
                    pass

                # check for down turn condition - cond 6
                elif self.isDownTurn(currPos, board, d) != False:
                    currPos, d = self.isDownTurn(currPos, board, d)
                    pass

                # step forward algo - cond 1
                else:
                    if d == 'up':
                        currPos, d = self.stepUp(currPos)
                    elif d == 'down':
                        currPos, d = self.stepDown(currPos)
                    elif d == 'right':
                        currPos, d = self.stepRight(currPos)
                    elif d == 'left':
                        currPos, d = self.stepLeft(currPos)
            else:
                return path, d

if __name__=="__main__":
    G = Game()
    board = G.gameBoard()[0]
    viewBoard = np.array(G.blankBoard())

    cancel = False
    while not cancel:
        start, d = G.rayStart()
        print('start', start)
        path = G.path(start, d, board)
        print(path)
	
