class TicTacToeBoard:
    def __init__(self):
        self.height = 3
        self.width = 3
        board = []

        # this is kinda stupid b/cits Y, X cords, to incrase Y by 1 to go down a row
        for row in range(self.height):
            board.append([])
            for col in range(self.width):
                board[row].append(None)

        self.board = board

    def get_state(self):
        return self.board

    def insert(self, mark, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = mark
            return True
        return False

    def check_winner(self, mark):
        c = "".join([mark, mark, mark])
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

        if None not in [self.board[0][2], self.board[1][1], self.board[2][0]]:
            row_val = "".join([self.board[0][2], self.board[1][1], self.board[2][0]])
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
