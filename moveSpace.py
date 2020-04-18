


def surrNode(currPos, board):
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



    
    # values surrounding currPos
    surr = [[board[II[0][0]][II[0][1]], board[I[0][0]][I[0][1]], board[II[1][0]][II[1][1]]],
            [board[I[2][0]][I[2][1]], board[row][col], board[I[3][0]][I[3][1]]],
            [board[II[2][0]][II[2][1]], board[I[1][0]][I[1][1]], board[II[3][0]][II[3][1]]]
            ]
    return surr
   


