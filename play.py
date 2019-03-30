from Environments.ticTacToeBoard import TicTacToeBoard
from Agents.player import Player
from copy import deepcopy #@todo - can get rid of, don't need in this file.
import time

# Init AI agent and board.
human_players_mark = "O"
ai_players_mark = "X"
ai_goes_first = True #todo - could make this a param.

board = TicTacToeBoard()
ai_player = Player(board, ai_players_mark, human_players_mark, ai_goes_first)
# ai_player2 = Player(board, "O", "X")

# AI player will go first
print("AI player taking turn....")
start_time = time.clock()
# For speed/ testing sake lets just set the first AI move to the middle square, set back to real later.
board.insert(ai_players_mark, 1, 1)
# ai_player.move()
print ("AI players turn took ", time.clock() - start_time, "seconds")
print("AI player has made there turn. Current board:")
board.print_state()
# board.print_state()

playing = True
human_players_turn = True
human_player_won = False
ai_player_won = False
directions = "Directions:"
valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "?", "p", "print", "exit"]
# get cords on board for number input.
input_to_cords_dict = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2],
}
# @todo - directions, ? logic and better validation


while playing:
    user_input = input(directions)

    if human_players_turn:
        # Validate input
        if user_input not in valid_input:
            print(user_input + " is not a valid input")

        else:

            if user_input.lower() == "exit":
                playing = False

            elif user_input.lower() in ["p", "print"]:
                board.print_state()

            elif user_input == "?":
                print(directions)

            else:
                board_cords = input_to_cords_dict[user_input]
                # mark players move on board, if illegal move notify user and let them try again.
                legal_move_made = board.insert(human_players_mark, board_cords[0], board_cords[1])
                # set to AI players turn turn
                if legal_move_made:

                    print("Current board after your move:")
                    board.print_state()

                    human_player_won = board.check_winner(human_players_mark)
                    if human_player_won:
                        print ("Congratulations! You won!")
                        playing = False
                        break

                    if board.is_board_full():
                        print ("Stalemate, try again")
                        playing = False
                        break

                    human_players_turn = False
                    print("AI player taking turn....")
                    start_time = time.clock()
                    ai_player.move()
                    print ("AI players turn took ", time.clock() - start_time, "seconds")
                    print("AI player has made there turn. Current board:")
                    board.print_state()

                    ai_player_won = board.check_winner(ai_players_mark)
                    if ai_player_won:
                        print ("The AI player has won, try again.")
                        playing = False
                        break

                    if board.is_board_full():
                        print ("Stalemate, try again")
                        playing = False
                        break

                    human_players_turn = True
                else:
                    print(user_input + " is not an empty space on the board, try again on an empty space.")
                    board.print_state()

    else:
        print("AI player taking turn.... please wait before entering any commands.")





# board.insert("1", 0, 0)
# board.insert("2", 0, 1)
# board.insert("3", 0, 2)
# board.insert("4", 1, 0)
# board.insert("5", 1, 1)
# board.insert("6", 1, 2)
# board.insert("7", 2, 0)
# board.insert("8", 2, 1)
# board.insert("9", 2, 2)
#
# board.print_state()




# board2 = None
# board3 = None

# # # Tests for evaluationfunction
# board.insert("X", 0, 2)
# board.insert("X", 1, 0)
# board.insert("X", 2, 2)
# board.insert("O", 0, 0)
# board.insert("O", 0, 1)
# board.insert("O", 2, 1)
# board.print_state()
# #
# ai_player2.move()
# board.print_state()
# # Tests for evaluationfunction end


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

