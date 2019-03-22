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

    # Cord 1 is row, cord2 is column
    def insert(self, mark, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = mark
            self.last_move = [cord1, cord2]
            return True
        return False

    def check_winner(self, mark):
        c = "".join([mark, mark, mark])
        rows = self.get_all_winning_rows()

        for row in rows:
            if None not in row:
                row_val = "".join(row)
                if c == row_val:
                    return True

        return False

    def get_empty_positions(self):
        # list of lists in [row, col] format
        empty_positions = []
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] is None:
                    empty_positions.append([row, col])
        return empty_positions

    def get_all_winning_rows(self):
        rows = []

        # Append for across wins
        for row in range(self.height):
            rows.append([self.board[row][0], self.board[row][1], self.board[row][2]])

        # Append for vertical wins
        for col in range(self.width):
            rows.append([self.board[0][col], self.board[1][col], self.board[2][col]])

        # Append for diagonal wins
        rows.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        rows.append([self.board[0][2], self.board[1][1], self.board[2][0]])

        return rows

    # used to get states idenfity states.
    # @todo - may be ablet o delete this is no reason to store duplicated states.
    def get_state_id(self):
        id = ""
        for row in range(self.height):
            for col in range(self.width):
                id += "+" if self.board[row][col] is None else self.board[row][col]
        return id

    def get_state(self):
        return self

    def print_state(self):
        for row in range(self.height):
            row_string = "|"
            for col in range(self.width):
                val = ' ' if self.board[row][col] is None else self.board[row][col]
                row_string = row_string + val + "|"
            print (row_string)
