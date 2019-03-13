class TicTacToeBoard:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        board = []

        for row in range(height):
            board.append([])
            for col in range(width):
                board[row].append(None)

        self.board = board

    def get_state(self):
        return self.board

    def insert_x(self, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = "X"
            return True
        return False

    def insert_o(self, cord1, cord2):
        if self.board[cord1][cord2] is None:
            self.board[cord1][cord2] = "O"
            return True
        return False

    def print_state(self):
        for row in range(self.height):
            row_string = "|"
            for col in range(self.width):
                val = ' ' if self.board[row][col] is None else self.board[row][col]
                row_string = row_string + val + "|"
            print (row_string)


board = TicTacToeBoard(3, 3)
board.insert_x(0,0)
board.insert_o(0,1)
board.print_state()