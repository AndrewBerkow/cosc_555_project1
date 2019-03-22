from Environments.ticTacToeBoard import TicTacToeBoard
from Agents.player import Player
from copy import deepcopy

board = TicTacToeBoard()
ai_player = Player(board, "X", "O")
ai_player2 = Player(board, "O", "X")

# board2 = None
# board3 = None

board.insert("X", 0, 2)
board.insert("X", 1, 0)
board.insert("X", 2, 2)
board.insert("O", 0, 0)
board.insert("O", 0, 1)
board.insert("O", 2, 1)
board.print_state()

ai_player2.move()
board.print_state()


# ai_player.move()
# board.print_state()

# for x in range(4):
#     ai_player.move()
#     board.print_state()
#     # print(board.check_winner("X"))
#     print(ai_player.evaluate_state())
#     print(board.get_state_id())
#
#     ai_player2.move()
#     board.print_state()
#     # print(board.check_winner("O"))
#     print(ai_player.evaluate_state())
#     print(board.get_state_id())
#
#     # if x == 1:
#     #     board2 = deepcopy(board)
#     #     print ("$$$$ BOARD 222222")
#     #     board2.print_state()
#     #
#     # if x == 2:
#     #     board3 = deepcopy(board)
#     #     print ("$$$$ BOARD 33333")
#     #     board3.print_state()
#     #     print ("$$$$ BOARD 222222")
#     #     board2.print_state()
#
#     # print ('empty pos')
#     # print(board.get_empty_positions())


# board3 = board.get_state()
# print ("$$$$ BOARD 33333")
# board3.print_state()
# print ("$$$$ BOARD 222222")
# board2.print_state()

# rows = board.get_all_winning_rows()
# print(*rows)

