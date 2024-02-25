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

    def __init__(self,r,c):
        self.rows = r
        self.columns = c
        self.board = np.empty((self.rows,self.columns),dtype='str')

    def display(self):
        print(self.board)

    def update(self,player_choice,player):
        if self.board[int(player_choice[0])-1,int(player_choice[1])-1]=='':
            self.board[int(player_choice[0])-1,int(player_choice[1])-1] = player
        else:
            print('This position is taken. Please give another position')
        return self.board

    #Row-wise Match check
    def across_check(self,player):
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
    # Column-wise Match check
    def below_check(self,player):
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
    def diagonal_check(self,player):
        if self.board[0,0]==player and self.board[1,1]==player and self.board[2,2]==player:
            print('Player {p} wins'.format(p=player))
            return False
        elif self.board[0,2]==player and self.board[1,1]==player and self.board[2,0]==player:
            print('Player {p} wins'.format(p=player))
            return False
        else:
            pass

input_board=list(input('Welcome to Tic-Tac-Toe Game. Select your desired dimension for the game in xy format.'))
board=Board(int(input_board[0]),int(input_board[1]))

def clear_screen():
    os.system('cls')

def setup_screen():
    clear_screen()
    board.display()

while True:
    setup_screen()
    x_choice=list(input("X) Where do you want to mark your position? Enter row and column number in xy format"))
    board.update(x_choice,'X')
    board.display()
    board.across_check('X')
    board.below_check('X')
    board.diagonal_check('X')
    print("---------------------------------")
    o_choice=list(input("O) Where do you want to mark your position? Enter row and column number in xy format"))
    board.update(o_choice,'O')
    board.display()
    board.across_check('X')
    board.below_check('O')
    board.diagonal_check('O')


