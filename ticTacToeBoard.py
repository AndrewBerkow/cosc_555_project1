class TicTacToeBoard:
    def __init__(self):
        self.height = 3
        self.width = 3
        board = []

        for row in range(self.height):
            board.append([])
            for col in range(self.width):
                board[row].append(None)

        self.board = board

    def get_state(self):
        return self.board

    def insert(self, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = "X"
            return True
        return False

    def insert(self, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = "O"
            return True
        return False

    def check_winner(self, player_x = True):
        c = "XXX" if player_x else "OOO"
        # Check for across wins
        for row in range(self.height):
            if None not in [self.board[row][0], self.board[row][1], self.board[row][2]]:
                row_val = "".join([self.board[row][0], self.board[row][1], self.board[row][2]])
                if  c == row_val:
                    return True

        # Check for vertical wins
        for col in range(self.width):
            if None not in [self.board[0][col], self.board[1][col], self.board[2][col]]:
                row_val = "".join([self.board[0][col], self.board[1][col], self.board[2][col]])
                if c == row_val:
                    return True

        # Check for diagonal wins
        if None not in [self.board[0][0], self.board[1][1], self.board[2][2]]:
            row_val = "".join([self.board[0][0], self.board[1][1], self.board[2][2]])
            if c == row_val:
                return True

        if None not in [self.board[0][0], self.board[1][1], self.board[2][2]]:
            row_val = "".join([self.board[2][2], self.board[1][1], self.board[2][0]])
            if c == row_val:
                return True

        return False

    def print_state(self):
        for row in range(self.height):
            row_string = "|"
            for col in range(self.width):
                val = ' ' if self.board[row][col] is None else self.board[row][col]
                row_string = row_string + val + "|"
            print (row_string)


board = TicTacToeBoard()
board.insert_x(0,0)
board.insert_o(0,1)
board.print_state()
board.insert_x(1, 0)
board.insert_x(2,0)
board.print_state()

print(board.check_winner())