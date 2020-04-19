import numpy as np

def surroundings(currPos, board):
    bSize = board.shape[0]
    row = currPos[0]
    col = currPos[1]

    # condition 1: row not in (0,7) and col not in (0, 7) ------------------------------------
    if row not in (0, bSize-1) and col not in (0, bSize-1):
        # indices [up-left, up, up-right]
        I = [(row-1, col-1), (row-1, col), (row-1, col+1)]
        # indices [left, right]
        II = [(row, col-1), (row, col), (row, col+1)]
        # indices [down-left, down, down-right]
        III = [(row+1, col-1), (row+1, col), (row+1, col+1)]


    # condition 2: row in (0, 7) col not in (0, 7) -------------------------------------------
    elif row == 0 and col not in (0, bSize-1):
        # off board indices
        I = [None, None, None]
        # indices [left, mid, right]
        II = [(row, col-1), (row, col), (row, col+1)]
        # indices [down-left, down, down-right]
        III = [(row+1, col-1), (row+1, col), (row+1, col+1)]

    elif row == bSize-1 and col not in (0, bSize-1):
        # indices [up-left, up, up-right]
        I = [(row-1, col-1), (row-1, col), (row-1, col+1)]
        # indices [left, right]
        II = [(row, col-1), (row, col), (row, col+1)]
        # off board indices
        III = [None, None, None]



    # condition 3: row not in (0, 7) col in (0, 7) -------------------------------------------
    elif row not in (0, bSize-1) and col == 0:
        # indices [None, up, up-right]
        I = [None, (row-1, col), (row-1, col+1)]
        # indices [None, mid, right]
        II = [None, (row, col), (row, col+1)]
        # indices [None, down, down-right]
        III = [None, (row+1, col), (row+1, col+1)]

    elif row not in (0, bSize-1) and col == bSize-1:
        # indices [up-left, up, None]
        I = [(row-1, col-1), (row-1, col), None]
        # indices [left, mid, None]
        II = [(row, col-1), (row, col), None]
        # indices [down-left, down, None]
        III = [(row+1, col-1), (row+1, col), None]


    # condition 4: row in (0, 7) col in (0, 7) ---------------------------------------------
    elif row == 0 and col == 0:
        # indices [None, None, None]
        I = [None, None, None]
        # indices [None, mid, right]
        II = [None, (row, col), (row, col+1)]
        # indices [None, down, down-right]
        III = [None, (row+1, col), (row+1, col+1)]

    elif row == bSize-1 and col == 0:
        # indices [None, up, up-right]
        I = [None, (row-1, col), (row-1, col+1)]
        # indices [None, mid, right]
        II = [None, (row, col), (row, col+1)]
        # indices [None, None, None]
        III = [None, None, None]

    elif row == 0 and col == bSize-1:
        # indices [None, None, None]
        I = [None, None, None]
        # indices [left, mid, None]
        II = [(row, col-1), (row, col), None]
        # indices [down-left, down, None]
        III = [(row+1, col-1), (row+1, col), None]

    elif row == bSize-1 and col == bSize-1:
        # indices [up-left, up, None]
        I = [(row-1, col-1), (row-1, col), None]
        # indices [left, mid, None]
        II = [(row, col-1), (row, col), None]
        # indices [None, None, None]
        III = [None, None, None]

    else:
        print("error")
        return 0

    arr = [I, II, III]
    tmp = []
    surr = []
    for i in arr:
        for pair in i:
            if pair != None:
                r, c = pair
                if r < bSize and r >= 0 and c < bSize and c >= 0:
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
