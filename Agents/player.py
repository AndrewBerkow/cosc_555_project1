import random
from copy import deepcopy
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
        self.log_mode = False

    def __init__(self, environment, mark, rival_mark):
        self.mark = mark
        self.rival_mark = rival_mark
        self.environment = environment
        self.log_mode = False

    def move(self):
        action = self.min_max_decision(self.environment)
        self.environment.insert(self.mark, action[0], action[1])
        #self.random_move()

    def set_log_mode(self, mode):
        self.log_mode = mode

    #returns an action
    '''
    next steps, need to generalize this and make it just action-pair value and have it not care about the cords or mark. 
    The possible actions array should detrmine rival vs your mark. 
    
    Than need alpha beta purnning
    
    Probably want an interface.
    
    In postmatorum write the hardest part was generalizing it. Improve to python standards. 
    
    Make an interface and parent class that is extended 3 times. Once just min max, 
    once AB pruning and once that keeps a hash of all states so no need to re compute values and go down these trees. 

    Do UI. 
    
    If I really get time than make it 5x5 or 7x7 and record times.
    '''
    def min_max_decision(self, state):

        possible_actions = self.get_possible_actions(state)

        # See what the state is after each action is done and pass into max_value function
        for action in possible_actions:
            state_after_action = deepcopy(state)
            state_after_action.insert(self.mark, action[0], action[1])
            action[2] = self.min_value(state_after_action)

        return max(possible_actions, key=lambda action: action[2])

    # return a utility vale
    def max_value(self, state):

        if self.terminal_test(state):
            return self.evaluate_state(state)

        possible_actions = self.get_possible_actions(state)

        # See what the state is after each action is done and pass into min_value function
        for action in possible_actions:
            state_after_action = deepcopy(state)
            state_after_action.insert(self.mark, action[0], action[1])
            action[2] = self.min_value(state_after_action)

        return max(possible_actions, key=lambda action: action[2])[2]

    # return a utility vale
    def min_value(self, state):

        if self.terminal_test(state):
            return self.evaluate_state(state)

        possible_actions = self.get_possible_actions(state)

        # See what the state is after each action is done and pass into min_value function
        for action in possible_actions:
            state_after_action = deepcopy(state)
            state_after_action.insert(self.rival_mark, action[0], action[1])
            action[2] = self.max_value(state_after_action)

        if self.log_mode:
            print("in min value function")
            print(*possible_actions)

        return min(possible_actions, key=lambda action: action[2])[2]


    def terminal_test(self, state):
        if self.log_mode:
            print("terminal test for")
            state.print_state()
        return len(state.get_empty_positions()) == 0 or state.check_winner(self.mark) or state.check_winner(self.rival_mark)


    # POSSIBLE ACTIONS STUFF
    def get_possible_actions(self, state):
        # Get cords of possible moves and add an empty index to the list to store the utility value
        possible_actions = []
        for action in state.get_empty_positions():
            action.append(None)
            possible_actions.append(action)
        return possible_actions

    ## EVALUATION STUFF
    # this may get moved to a different object, also should renaem evaluation function.
    def evaluate_state(self, state):
        utility = 0
        winning_rows = state.get_all_winning_rows()
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
        Evaluation function source https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html
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



