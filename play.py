from Environments.ticTacToeBoard import TicTacToeBoard
from Agents.player import Player

board = TicTacToeBoard()
ai_player = Player(board, "X", "O")
ai_player2 = Player(board, "O", "X")

for x in range(4):
    ai_player.move()
    board.print_state()
    # print(board.check_winner("X"))
    print(ai_player.evaluate_state())

    ai_player2.move()
    board.print_state()
    # print(board.check_winner("O"))
    print(ai_player.evaluate_state())

    # print ('empty pos')
    # print(board.get_empty_positions())

# rows = board.get_all_winning_rows()
# print(*rows)

