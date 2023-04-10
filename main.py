class connectFour:
    def __init__(self, board):
        self.board = board

    def rowCheck(self, board, turn):
        for row in range(len(board)):
            rows = []
            for col in range(len(board)):
                if board[row][col] == turn:
                    rows.append(board[row][col])
            if len(rows) == 4:
                if len(set(rows)) == 1:
                    return rows[0]
        return False

    def checkCol(self, board,turn):
        for row in range(len(board)):
            rows = []
            for col in range(len(board[0]) - 1):
                if board[col][row] == turn:
                    rows.append(board[col][row])
            if len(rows) == 4:
                if len(set(rows)) == 1:
                    return rows[0]
        return False

    def checkFirstDiagonal(self, board,turn):
        rows = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == col:
                    if board[row][col] == turn:
                        rows.append(board[row][col])
        if len(rows) == 4:
            if len(set(rows)) == 1:
                return rows[0]
        return False

    def checkSecondDiagonal(self, board,turn):
        r, c = 0, len(board[0]) - 1
        rows = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == r and col == c:
                    if board[row][col] == turn:
                        rows.append(board[row][col])
            r += 1
            c -= 1
        if len(rows) == 4:
            if len(set(rows)) == 1:
                return rows[0]
        return False

    def printBoard(self, board):
        for row in board:
            for col in row:
                print(col,"|",end=" ")
            print()

    def checkWin(self, board,turn):
        result1 , result2 = self.rowCheck(board,turn) , self.checkCol(board,turn)
        result3 , result4 = self.checkFirstDiagonal(board,turn) , self.checkSecondDiagonal(board,turn)
        if result1 != False:
            print(result1, "wins.")
            return True
        if result2 != False:
            print(result2, "wins.")
            return True
        if result3 != False:
            print(result3, "wins.")
            return True
        if result4 != False:
            print(result4, "wins")
            return True

    def Main(self):
        t = 0
        print("This game consist of 2 players.The first player disk is R and second player disk is Y"
              ".You have to enter the row and column for your position.")
        self.printBoard(self.board)
        while True:
            player1 = input(("It's player 1 turn.Enter row and column :")).split()
            if self.board[int(player1[0]) - 1][int(player1[1]) - 1] == " ":
                self.board[int(player1[0]) - 1][int(player1[1]) - 1] = "R"
                t += 1
                self.printBoard(self.board)
                if self.checkWin(self.board,"R"):
                    break
            else:
                print("Please select the position which is empty.")
            player2 = input("It's player 2 turn.Enter row and column:").split()
            if self.board[int(player2[0]) - 1][int(player2[1]) - 1] == " ":
                self.board[int(player2[0]) - 1][int(player2[1]) - 1] = "Y"
                t += 1
                self.printBoard(self.board)
                if self.checkWin(self.board,"Y"):
                   break
            else:
                print("Please select the position which is empty.")
            if t == 42:
                print("Match draws.")
                break

obj = connectFour([[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "]])
obj.Main()

