import numpy as np
import os

class TictacToe:

    def __init__(self):
        self.rows = None
        self.cols = None
        self.player='X'
        print('Welcome to Tic-Tac-Toe Game')
    
    def setRows(self,rows):
        self.rows=rows
    def setCols(self,cols):
        self.cols=cols
    def getRows(self):
        return self.rows
    def getCols(self):
        return self.cols

    def start_game(self):
        while True:
            i_rows=input('How many rows do you want ?')
            i_cols=input('How many columns do you want ?')
            if self.is_valid([i_rows,i_cols]):
                self.setRows(int(i_rows))
                self.setCols(int(i_cols))
                self.set_reset_board()
                break

    def is_valid(self,input_list):
        if input_list[0].isdigit() and input_list[-1].isdigit():
            return True
        else:
            print('Invalid input. Please give only numbers')
            return False
    
    def set_reset_board(self):
        self.board = np.full((self.rows,self.cols),' ',dtype='str')
        self.display_board()
        self.play_game()
    
    def display_board(self):
       list_view=[[self.board[i,j] for j in range(self.board.shape[1])] for i in range(self.board.shape[0])]
       for row in list_view:
            print("|".join(row))
            print("-"*(self.board.shape[1]+3))


    def player_input(self,player):
        while True:
            player_choice=input("{player}'s turn: Where do you want to mark your position? Enter row and column number in x,y format".format(player=player))
            if self.player_choice_validations(player_choice):
                return player_choice.split(',')
            
    def player_choice_validations(self,player_choice):
        player_choice_re=player_choice.split(',')
        if self.player_choice_prelim_validation(player_choice) and self.is_valid(player_choice_re) and self.fits_board(player_choice_re) and self.player_choice_fill_check(player_choice_re):
            return True
        else:
            return False
    
    def player_choice_prelim_validation(self,player_choice):
        if ',' in player_choice: # checks if given in x,y format
            player_choice = player_choice.split(',')
            return player_choice
        else:
            print("Please give your choice in x,y format")
            return False

    
    def switch_players(self):
        self.player='O' if self.player =='X' else 'X'
    

    def play_game(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            player_choice=self.player_input(self.player) # gets the player_choice in right format
            self.update_board(player_choice)   # updates the board
            self.display_board() # displays the updated board
            if self.is_win():  # check for win
                self.display_board()
                self.end_game()
                break
            else:
                print('Swapping players')
                self.switch_players()

    
    def end_game(self):
        while(True):
            play_again = input("Do you want to play again? Give Y/N")
            if play_again.upper()=='Y':
                self.player='X'
                self.start_game()
                break
            elif play_again.upper()=='N':
                print('Hope you have enjoyed the game')
                break
            else:
                print("Invalid input. Please give y or n")

    
    def fits_board(self,player_choice):
        if int(player_choice[0])<=self.rows and int(player_choice[-1])<=self.cols:
            return True
        else:
            print('Input does not fit the board. Please give x,y fitting the board size {r},{c}'.format(r=self.rows,c=self.cols))
            return False
        
    def is_win(self):
        if self.match_check() or self.match_tie_check():
            return True
        else:
            return False
        
    def player_choice_fill_check(self,player_choice):
         #checks if a player_choice position is not filled
         if self.board[int(player_choice[0])-1,int(player_choice[-1])-1]==' ':
            return True
         else:
            print('This position is taken. Please give another position')
            return False
             

             
    def update_board(self,player_choice):
        self.board[int(player_choice[0])-1,int(player_choice[-1])-1] = self.player
        

    def match_check(self):
        if self.across_check() or self.below_check() or self.diagonal_check():
            print('{player} wins!'.format(player=self.player))
            return True
        else:
            return False
        
    def match_tie_check(self):
        filled_spots = np.count_nonzero(self.board!=' ')
        if filled_spots == self.rows*self.cols:
            print('The match is tied')
            return True
        else:
            return False

    
    #Row-wise Match check
    def across_check(self):
        for i in range(0,self.board.shape[0]):#row
            c=0
            for j in range(0,self.board.shape[1]):#column
                if j<self.board.shape[1]-1: #should be 1 less than no.of cols
                    if self.board[i,j] == self.player and self.board[i,j+1] == self.player:
                        c+=1
            if c==self.board.shape[1]-1:
                print('Player {p} wins'.format(p=self.player))
                return True
            else:
                continue
    
    # Column-wise Match check
    def below_check(self):
        for i in range(0,self.board.shape[1]):#column
            d=0
            for j in range(0,self.board.shape[0]):#row
                if j<self.board.shape[0]-1: #4-1=3
                    if self.board[j,i]==self.player and self.board[j+1,i]==self.player:#2=3
                        d+=1
            if d==self.board.shape[0]-1:
                print('Player {p} wins!'.format(p=self.player))
                return True    
            else:
                continue

        
    def diagonal_check(self): # Update=ing any dimension game
        # Check main diagonal (top-left to bottom-right)
        main_diagonal = [self.board[i, i] for i in range(min(self.rows, self.cols))]
        if all(symbol == self.player for symbol in main_diagonal):
            print('Player {p} wins!'.format(p=self.player))
            return True

        # Check secondary diagonal (top-right to bottom-left)
        secondary_diagonal = [self.board[i, self.cols - i - 1] for i in range(min(self.rows, self.cols))]
        if all(symbol == self.player for symbol in secondary_diagonal):
            print('Player {p} wins!'.format(p=self.player))
            return True
                 
    
if __name__ == "__main__":
    tk = TictacToe()
    tk.start_game()

    