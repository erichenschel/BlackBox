# list of nodes along the path of ray
    def rayPath(self, start, board):
        path = []
        currNode = None
        currPos = 0
        exit = False

        def moveUp(node):
            row = node[0]
            col = node[1]
            return row-1, col

        def moveDown(node):
            row = node[0]
            col = node[1]
            return row+1, col

        def moveRight(node):
            row = node[0]
            col = node[1]
            return row, col+1

        def moveLeft(node):
            row = node[0]
            col = node[1]
            return row, col-1
        
        while not exit:
            
            # moving down

            # rays current position on board is start
            if currPos == 0:
                row = start[0]
                col = start[1]

                # starting space is empty
                if board[row][col] == 0:
                    path.append(start)
                    currPos +=1

                # (hit) starting space is a force field right above node
                elif board[row][col] == 1 and board[row+1][col] == 2:
                    path.append(start)
                    # break loop
                    exit = True

                # (hit) starting space is occupied by a node
                else:
                    # break loop
                    exit = True

            # currPos != start (path array is not empty)
            else:
                row = path[currPos][0]
                col = path[currPos][1]
                print(row, col)

                #







            # moving down -- change row (increase)
            # direct hit (node on edge of board)
            if board[row][col] == 2:
                return path
            # able to occupy the first space but node is in next space
            elif board[row+1][col] == 2:
                row = (row, col)
                currPos = (row, col)
                path.append(currPos)
                return path

            # reflection - to the right
            if board[row][col] == 1 and board[row][col-1] == 2:
                currPos = (row, col)
                path.append(currPos)
                return path

            # reflection - to the left
            if board[row][col] == 1 and board[row][col+1] == 2:
                col += 1
                currPos = (row, col)
                path.append(currPos)

                # deflection - right
            if board[row][col] == 1 and board[row+1][col-1] == 2:
                col += 1
                currPos = (row, col)
                path.append(currPos)
            # deflection - left
            if board[row][col] == 1 and board[row+1][col+1] == 2:
                col -= 1
                currPos = (row, col)
                path.append(currPos)



           # -------------------------------------------------------
            # moving up -- change row (decrease)
            if row == self.boardSize-1:
                # hit
                if board[row][col] == 2 or board[row-1][col] == 2:
                    return 0

                # reflection - to the right
                if board[row][col] == 1 and board[row][col-1] == 2:
                    return 0

                # reflection - to the left
                if board[row][col] == 1 and board[row][col+1] == 2:
                    return 0

                # deflection - right
                if board[row][col] == 1 and board[row-1][col-1] == 2:
                    return 0

                # deflection - left
                if board[row][col] == 1 and board[row-1][col+1] == 2:
                    return 0




