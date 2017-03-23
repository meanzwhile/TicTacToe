import os
from random import randint


def generate_board(board_size):
    the_list = []
    for i in range(board_size):
        temp_list = []
        for j in range(board_size):
            temp_list.append(str(j+board_size*i))
        the_list.append(temp_list)
    return the_list


def draw_board(board_as_list):
    print("-"+"-"*(4*len(board_as_list)))
    for row in range(len(board_as_list)):
        for number in range(len(board_as_list)):
            if len(board_as_list[row][number]) == 1:
                board_as_list[row][number] = " " + board_as_list[row][number] + " "
            if len(board_as_list[row][number]) == 2:
                board_as_list[row][number] = " " + board_as_list[row][number]
        print("|"+str("|".join(board_as_list[row])+"|"))
        print("-"+"-"*(4*len(board_as_list)))


def check_if_occupied(board_as_list, position):
    position1 = int(int(position) / len(board_as_list))
    position2 = int(position) % len(board_as_list)
    if board_as_list[position1][position2] == " X ":
        return False
    if board_as_list[position1][position2] == " O ":
        return False
    else:
        return True


def choose_letter(board_as_list):
    max_size = (len(board_as_list) * len(board_as_list))
    position = -1
    while position not in range(0, max_size) or not check_if_occupied(board_as_list, position):
        print("Select a valid number between 1-" + str(max_size-1))
        try:
            position = int(input())
        except:
            pass
    if len(str(position)) == 1:
        position = " " + str(position) + " "
    if len(str(position)) == 2:
        position = " " + str(position)
    return str(position)


def put_letter(board_as_list, letter):
    position = choose_letter(board_as_list)
    for i in range(len(board_as_list)):
        for j in range(len(board_as_list)):
            if board_as_list[i][j] == position:
                board_as_list[i][j] = letter
                break


def win_condition_column(board_as_list, letter):
    j = 0
    while j < len(board_as_list):
        i = 0
        while i < len(board_as_list) and board_as_list[i][j] == letter:
            i += 1
            if i == len(board_as_list):
                return True
        j += 1
    else:
        return False


def win_condition_row(board_as_list, letter):
    for i in range(len(board_as_list)):
        if all(x == letter for x in board_as_list[i]):
            return True
    else:
        return False


def win_condition_cross(board_as_list, letter):
    i = 0
    while i < len(board_as_list) and board_as_list[i][i] == letter:
        i += 1
        if i == len(board_as_list):
            return True
    else:
        return False


def win_condition_reverse_cross(board_as_list, letter):
    i = 0
    j = len(board_as_list)-1
    while i < len(board_as_list) and board_as_list[i][j] == letter:
        i += 1
        j -= 1
        if i == len(board_as_list):
            return True
    else:
        return False


def ultimate_win_condition(board_as_list, letter):
    if win_condition_column(board_as_list, letter) is True:
        return True
    if win_condition_row(board_as_list, letter) is True:
        return True
    if win_condition_cross(board_as_list, letter) is True:
        return True
    if win_condition_reverse_cross(board_as_list, letter) is True:
        return True
    else:
        return False


def change_turn(letter):
    if letter == " X ":
        return " O "
    else:
        return " X "


def print_starter_screen():
    os.system("clear")
    print("Welcome to T.T.T.E.!".center(110))
    print("(Tic Tac Toe Extreme)".center(110))
    print("Where you can choose the board's size !!!".center(110))
    print("\n\n\n\n")


def main():
    tablesize = 0
    counter = 0
    while tablesize not in range(3, 11):
        print("Enter the table size (x*x)\n(Between 3-10) ")
        try:
            tablesize = int(input())
        except:
            pass
    the_board = generate_board(tablesize)
    letter = " X "
    if randint(0, 1) == 0:
        actual_player_name = player_1_name
    else:
        actual_player_name = player_2_name
    turn_is_on = True
    while turn_is_on:
        os.system("clear")
        print("It's your turn " + actual_player_name + "  (" + letter + ")")
        draw_board(the_board)
        put_letter(the_board, letter)
        if ultimate_win_condition(the_board, letter) is True:
            if actual_player_name == player_1_name:
                print(player_1_name + " won the round!")
                return 1
            else:
                print(player_2_name + " won the round!")
                return 2
            draw_board(the_board)
            turn_is_on = False
        letter = change_turn(letter)
        if actual_player_name == player_1_name:
            actual_player_name = player_2_name
        else:
            actual_player_name = player_1_name
        counter += 1
        if counter == tablesize * tablesize:
            return 3


if __name__ == '__main__':
    player_1_score = 0
    player_2_score = 0
    tie_score = 0
    print_starter_screen()
    playing_the_game = True
    print("Enter first player's name: ")
    player_1_name = input()
    print("Enter second player's name: ")
    player_2_name = input()
    os.system("clear")

    while playing_the_game is True:
        winner = 0
        winner = main()
        if winner == 1:
            player_1_score += 1
        if winner == 2:
            player_2_score += 1
        if winner == 3:
            tie_score += 1

        print(str(player_1_name) + " : " + str(player_1_score) + "   Ties : " + str(tie_score)+"   " + str(player_2_name) + " : " + str(player_2_score))
        player_answer = ""
        while (player_answer is not "y") and (player_answer is not "n"):
            print("Do you want to play again? (y/n)")
            player_answer = input()
        if player_answer == "n":
            playing_the_game = False
        if player_answer == "y":
            playing_the_game = True
