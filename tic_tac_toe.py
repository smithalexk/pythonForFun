def get_cell_input():
    return input("Enter cells: >")
    
def only_one_true(iterable):
    i = iter(iterable)
    return any(i) and not any(i)

def get_user_input():
    cell_input = input("Enter the Coordinates: > ").split(" ")
    try:
        return [int(x)-1 for x in cell_input]
    except ValueError:
        print("You should enter numbers!")
        return get_user_input()
    
def compare_input_to_board(board_state, turn):
    user_input = get_user_input()
    rows = [board_state[6:], board_state[3:6], board_state[0:3]]
    if user_input[0] < 0 or user_input[0] > 2 or user_input[1] < 0 or user_input[1] > 2:
        print("Coordinates should be from 1 to 3!")
        return compare_input_to_board(board_state, turn)
    elif rows[user_input[1]][user_input[0]] is not "_":
        print("This cell is occupied! Choose another one!")
        return compare_input_to_board(board_state, turn)
    else:
        row_list = [x for x in rows[user_input[1]]]
        row_list[user_input[0]] = turn
        rows[user_input[1]] = ''.join(row_list)
        return ''.join([rows[2], rows[1], rows[0]])
        

def check_status(output):
    n_x = output.count('X')
    n_o = output.count("O")
    if abs(n_x - n_o) > 1:
        print("Impossible")
        return True
    
    rows = [output[0:3], output[3:6], output[6:]]
    cols = [output[0::3], output[1::3], output[2::3]]
    diag1 = output[0] + output[4] + output[-1]
    diag2 = output[2] + output[4] + output[-3]
    
    row_win = [x.count(x[0]) == len(x) and x[0] is not "_" for x in rows]
    col_win = [x.count(x[0]) == len(x) and x[0] is not "_" for x in cols]
    diag_win = [x.count(x[0]) == len(x) and x[0] is not "_" for x in [diag1, diag2]]
    
    if only_one_true(row_win + col_win + diag_win):
        if any([True if "XXX" in x else False for x in [rows, cols, diag1, diag2]]):
            print_board(output)
            print("X wins")
            return True
        else:
            print_board(output)
            print("O wins")    
            return True
    elif not any(row_win + col_win + diag_win):
        if any([True if "_" in x else False for x in rows + cols + [diag1, diag2]]):
            return False
        else:
            print_board(output)
            print("Draw")
            return True
    else:
        print("Impossible")
        return True
    
    return
    
    
def print_board(output):
    print('---------')
    print(f"| {output[0]} {output[1]} {output[2]} |")
    print(f"| {output[3]} {output[4]} {output[5]} |")
    print(f"| {output[6]} {output[7]} {output[8]} |")
    print('---------')
    # print_status(output)

def run_game():
    board_state = 9*"_"
    
    Finished = False
    turn = "O"
    while not Finished:

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        print_board(board_state)
        board_state = compare_input_to_board(board_state, turn)
        Finished = check_status(board_state)
    

        
    


run_game()
