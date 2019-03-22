class Player:
    def __init__(self, environment, player_x = True):
        self.mark = "X" if player_x else "0"
        self.environment = environment

    def move(self):
        return True



