import random
'''
PEAS Description for player agent in a game of tic tac toe.
Performance measure:
Environment: ticTacToeBoard object
Actuators: Make move
Sensors: Game is fully observable and the play can get access to the state at any time.
'''

class Player:
    def __init__(self, environment):
        self.mark = "X"
        self.rival_mark = "O"
        self.environment = environment

    def __init__(self, environment, mark, rival_mark):
        self.mark = mark
        self.rival_mark = rival_mark
        self.environment = environment

    def move(self):
        self.random_move()

    # this may get moved to a different object, also should renaem evaluation function.
    def evaluate_state(self):
        utility = 0
        winning_rows = self.environment.get_all_winning_rows()
        for row in winning_rows:
            utility += self.evaluate_row(row)
        return utility

    def evaluate_row(self, row):
        row_utility = 0
        marked_three = "".join([self.mark, self.mark, self.mark])
        marked_two = "".join([self.mark, self.mark])
        rival_marked_three = "".join([self.rival_mark, self.rival_mark, self.rival_mark])
        rival_marked_two = "".join([self.rival_mark, self.rival_mark])
        '''
        evaluation function source https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html
        +100 for EACH 3-in-a-line for computer.
        +10 for EACH 2-in-a-line (with a empty cell) for computer.
        +1 for EACH 1-in-a-line (with two empty cells) for computer.
        Negative scores for opponent, i.e., -100, -10, -1 for EACH opponent's 3-in-a-line, 2-in-a-line and 1-in-a-line.
        0 otherwise (empty lines or lines with both computer's and opponent's seed).
        '''

        # check for 3 in a row, can just return if found
        if None not in row:
            if "".join(row) == marked_three:
                return 100
            elif "".join(row) == rival_marked_three:
                return -100

        # check row two in a row
        if row[0] == self.mark and row[1] == self.mark or row[1] == self.mark and row[2] == self.mark:
            row_utility += 10
            if self.rival_mark in row:
                row_utility += -1 #if its two in a row, that means only one left so its faster to just check to see if that last one is rivals mark
            return row_utility

        if row[0] == self.rival_mark and row[1] == self.rival_mark or row[1] == self.rival_mark and row[2] == self.rival_mark:
            row_utility += -10
            if self.mark in row:
                row_utility += -1
            return row_utility

        for pos in range(3):
            if row[pos] is not None:
                row_utility += 1 if row[pos] == self.mark else -1

        return row_utility

    def random_move(self):
        legal_move_made = False
        while not legal_move_made:
            xcord = random.randint(0, 2)
            ycord = random.randint(0, 2)
            legal_move_made = self.environment.insert(self.mark, xcord, ycord)

        return True



