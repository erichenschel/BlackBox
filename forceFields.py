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
