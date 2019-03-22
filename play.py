from Environments.ticTacToeBoard import TicTacToeBoard
from Agents.player import Player

board = TicTacToeBoard()
ai_player = Player("X")

# ai_player.move()
# board.print_state()
# print(board.check_winner("X"))
#
# move(board)
# board.print_state()
# print(board.check_winner("O"))

board.insert("X", 0, 0)
board.print_state()
print(board.check_winner("X"))

board.insert("O", 0, 1)
board.print_state()
print(board.check_winner("O"))


board.insert("X", 1, 0)
board.print_state()
print(board.check_winner("X"))

board.insert("X", 2, 0)
board.print_state()
print(board.check_winner("X"))

board.insert("O", 1, 1)
board.print_state()
print(board.check_winner("O"))

board.insert("O", 2, 1)
board.print_state()
print(board.check_winner("O"))

#
# def move(board):
#     legal_move_made = False
#     while not legal_move_made:
#         xcord = random.randint(0, 3)
#         ycord = random.randint(0, 3)
#         legal_move_made = self.environment.insert("0", xcord, ycord)
#     return True

