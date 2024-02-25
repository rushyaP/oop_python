import numpy as np
class Board:

    def __init__(self,r,c):
        self.rows = r
        self.columns = c
        self.board = np.empty((self.rows,self.columns),dtype='str')

    def display(self):
        print(self.board)

input_board=list(input("Welcome to Tic-Tac-Toe Game. Select your desired dimension for the game in xy format."))
print(input_board)
board=Board(int(input_board[0]),int(input_board[1]))

