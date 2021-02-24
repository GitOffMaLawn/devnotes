#!/bin/env python3

import random

board_spaces_dict = {'a1': 'a1', 'a2': 'a2', 'a3': 'a3', 'b1': 'b1', 'b2': 'b2', 'b3': 'b3', 'c1': 'c1', 'c2': 'c2', 'c3': 'c3'}
db_dict = {'a1': '_', 'a2': '_', 'a3': '_', 'b1': '_', 'b2': '_', 'b3': '_', 'c1': '_', 'c2': '_', 'c3': '_'}
x = 'X'
o = 'O'

def draw_board(move = None, piece = ''):
    board_spaces_dict.pop(move)
    db_dict[move] = piece
    print("  a   b   c ")
    print(f"1_{db_dict['a1']}_|_{db_dict['b1']}_|_{db_dict['c1']}_")
    print(f"2_{db_dict['a2']}_|_{db_dict['b2']}_|_{db_dict['c2']}_")
    print(f"3 {db_dict['a3']} | {db_dict['b3']} | {db_dict['c3']} ")

def computer_move(c_move, c_piece):
    print(f"Computer has thought long and hard, it has chosen {c_move}")
    draw_board(c_move, c_piece)
    # computer look at dictionary to see what is empty
    # random.choice(seq)
    # Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

def player_move(p_piece):
    print("Player's turn, select the move by entering the coordinates. eg: b2 ")
    p_move = input(f"You are the {p_piece} piece, select your coordinates:").lower()
    # decide if valid move
    return draw_board(p_move, p_piece)

def random_pick_turn():
    print("Welcome to TicTacToe, first to get three X's or O's in a row, WINS!")
    print("We flipped a coin to see who plays first...")
    rp = random.randint(0, 2)
    if rp == 0:
        # Human is 'O'
        print("Computer plays First with 'X'!")
    else:
        print("Player plays First with 'X'!")
        print("  a   b   c ")
        print(f"1_{db_dict['a1']}_|_{db_dict['b1']}_|_{db_dict['c1']}_")
        print(f"2_{db_dict['a2']}_|_{db_dict['b2']}_|_{db_dict['c2']}_")
        print(f"3 {db_dict['a3']} | {db_dict['b3']} | {db_dict['c3']} ")
        # return X always plays first, hp or cp
    return rp

def test_winner(h_player):
    ## X wins start here
    if db_dict['a1'] == 'X' and db_dict['b1'] == 'X' and db_dict['c1'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
            
    elif db_dict['a2'] == 'X' and db_dict['b2'] == 'X' and db_dict['c2'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['a3'] == 'X' and db_dict['b3'] == 'X' and db_dict['c3'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['a1'] == 'X' and db_dict['a2'] == 'X' and db_dict['a3'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['b1'] == 'X' and db_dict['b2'] == 'X' and db_dict['b3'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['c1'] == 'X' and db_dict['c2'] == 'X' and db_dict['c3'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['a1'] == 'X' and db_dict['b2'] == 'X' and db_dict['c3'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    elif db_dict['a3'] == 'X' and db_dict['b2'] == 'X' and db_dict['c1'] == 'X':
        if h_player == 0:
            print("Computer Wins!")
            return True
        else:
            print("Human Wins!")
            return True
        
    ## O start here
    elif db_dict['a1'] == 'O' and db_dict['b1'] == 'O' and db_dict['c1'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a2'] == 'O' and db_dict['b2'] == 'O' and db_dict['c2'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a3'] == 'O' and db_dict['b3'] == 'O' and db_dict['c3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a1'] == 'O' and db_dict['a2'] == 'O' and db_dict['a3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['b1'] == 'O' and db_dict['b2'] == 'O' and db_dict['b3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['c1'] == 'O' and db_dict['c2'] == 'O' and db_dict['c3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a1'] == 'O' and db_dict['b2'] == 'O' and db_dict['c3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a1'] == 'O' and db_dict['b2'] == 'O' and db_dict['c3'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    elif db_dict['a3'] == 'O' and db_dict['b2'] == 'O' and db_dict['c1'] == 'O':
        if h_player == 0:
            print("Human Wins!")
            return True
        else:
            print("Computer Wins!")
            return True
        
    else:
        return False

def start_game():
    pick = random_pick_turn()
    while test_winner(pick) == False:
        if len(board_spaces_dict) == 0:
            print("IT'S A STALEMATE!")
            break
        elif pick == 0:
            # Human is 'O'
            computer_move(random.choice(list(board_spaces_dict)), x)
            player_move(o)
        else:
            # Human is 'X'
            player_move(x)
            computer_move(random.choice(list(board_spaces_dict)), o)


start_game()
