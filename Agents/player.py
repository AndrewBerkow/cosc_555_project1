import random
'''
PEAS Description for player agent in a game of tic tac toe.
Performance measure:
Environment: ticTacToeBoard object
Actuators: Make move
Sensors: Game is fully observable and the play can get access to the state at any time.
'''

class Player:
    def __init__(self, environment, mark):
        self.mark = mark
        self.environment = environment

    def move(self):
        legal_move_made = False
        while not legal_move_made:
            xcord = random.randint(0,2)
            ycord = random.randint(0, 2)
            legal_move_made = self.environment.insert(self.mark, xcord, ycord)

        return True



