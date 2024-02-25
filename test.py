"""
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def create_board(size=3):
    return [[" " for _ in range(size)] for _ in range(size)]

# Example usage
board = create_board()
print_board(board)
"""
import os
import numpy as np
class Board:

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = np.empty((self.rows,self.columns),dtype='str')

    def display_board(self):
        return self.board

    def update_board(self,player_choice,player):
        if self.board[int(player_choice[0])-1,int(player_choice[1])-1]=='':
            self.board[int(player_choice[0])-1,int(player_choice[1])-1] = player
        else:
            print('This position is taken. Please give another position')
        return self.display_board()
    

    #Across Match check
    def across_board_check(self,player):
        for i in range(0,self.board.shape[0]):#row
            c=0
            for j in range(0,self.board.shape[1]):#column
                if j!=2:
                    if self.board[i,j] == player and self.board[i,j+1] == player:
                        c+=1
            if c==self.board.shape[0]-1:
                print('Player {p} wins'.format(p=player))
                break    
            else:
                continue
    # Below Match check
    def below_board_check(self,player):
        for i in range(0,self.board.shape[0]):#column
            d=0
            for j in range(0,self.board.shape[1]):#row
                if j!=2:
                    if self.board[j,i]==player and self.board[j+1,i]==player:
                        d+=1
            if d==self.board.shape[0]-1:
                print('Player {p} wins'.format(p=player))
                break    
            else:
                continue

    # Diagonal Match check
    def diagonal_board_check(self,player):
        if self.board[0,0]==player and self.board[1,1]==player and self.board[2,2]==player:
            print('Player {p} wins'.format(p=player))
            return False
        elif self.board[0,2]==player and self.board[1,1]==player and self.board[2,0]==player:
            print('Player {p} wins'.format(p=player))
            return False
        else:
            pass

def clear_screen():
    os.system('cls')

clear_screen()

input("Welcome to Tic-Tac-Toe Game. Select your desired dimension for the game. Press Enter to Continue")
b=Board()
print(b.display_board())

while True:
    x_choice=list(input("X) Where do you want to mark your position? Enter row and column number in xy format"))
    b.update_board(x_choice,'X')
    

    b.below_board_check('X')
    b.diagonal_board_check('X')


    o_choice=list(input("O) Where do you want to mark your position? Enter row and column number in xy format"))
    y=b.update_board(o_choice,'O')
    print(y)

    b.below_board_check('O')
    b.diagonal_board_check('O')


