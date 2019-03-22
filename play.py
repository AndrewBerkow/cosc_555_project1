from Environments.ticTacToeBoard import TicTacToeBoard
from Agents.player import Player

board = TicTacToeBoard()
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

