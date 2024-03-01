import numpy as np
class TictacToe:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def start_game(self):
        input_board=list(input('Welcome to Tic-Tac-Toe Game. Select your desired dimension for the game in xy format.'))
        self.set_reset_board(int(input_board[0]),int(input_board[-1]))
    
    def set_reset_board(self,rows,cols):
        self.board = np.full((rows,cols),' ',dtype='str')
        self.display_board(self.board)
        self.play_game()
    
    def display_board(self,board):
       print('before lsit view')
       list_view=[[board[i,j] for j in range(board.shape[1])] for i in range(board.shape[0])]
       print('after list view')
       for row in list_view:
            print("|".join(row))
            print("-"*(board.shape[1]+3))

    def some_func(self):
        while(True):
            board_upd_st=self.update_board(x_choice,'X')
            if not board_upd_st:
                print('Regive')
            self.display_board(self.board)
            if self.match_check('X'):
                self.end_game()
                break

    def player_x_input(self):
        print('here')
        x_choice=list(input("\nX) Where do you want to mark your position? Enter row and column number in xy format"))
        self.update_board(x_choice,'X')
        #return x_choice
    
    def player_o_input(self):
        o_choice=list(input("\nO) Where do you want to mark your position? Enter row and column number in xy format"))
        self.update_board(o_choice,'O')
        #return o_choice

    def play_game(self):
        print('play func begining')
        while True:
            self.player_x_input()
            self.player_o_input()
        """
        while True:
            x_choice=list(input("\nX) Where do you want to mark your position? Enter row and column number in xy format"))
            #if x_choice[0]<=self.rows and x_choice[-1]<=self.cols
            if self.board[int(x_choice[0])-1,int(x_choice[-1])-1]==' ':
                board_upd_st=self.update_board(x_choice,'X')
                self.display_board(self.board)
                if self.match_check('X'):
                    self.end_game()
                    break
            else:
                print('Regive')
            
        
        while True:            
            o_choice=list(input("\nO) Where do you want to mark your position? Enter row and column number in xy format"))
            self.update_board(o_choice,'O')
            self.display_board(self.board)
            if self.match_check('O'):
                self.end_game()
                break
            """ 

    def end_game(self):
        while(True):
            play_again = input("Do you want to play again? Give Y/N")
            if play_again.upper()=='Y':
                self.start_game()
                break
            elif play_again.upper() not in ['Y','N']:
                print("Invalid input. Please give y or n")
            else:
                print('Hope you have enjoyed the game')
                break
                #return False
                

    def update_board(self,player_choice,player):
        while True:
            if self.board[int(player_choice[0])-1,int(player_choice[-1])-1]==' ':
                self.board[int(player_choice[0])-1,int(player_choice[-1])-1] = player
                self.display_board(self.board)
                if self.match_check(player) or self.match_tie_check():
                    self.end_game()
                    #break
            else:
                print('This position is taken. Please give another position')
                if player=='X':
                    self.player_x_input()
                else:
                    self.player_o_input()
            return False

    def match_check(self,player):
        if self.across_check(player) or self.below_check(player) or self.diagonal_check(player):
            return True
        else:
            return False
        
    def match_tie_check(self):
        c=0
        for r in range(0,len(self.board)):
            print('rows',len(self.board))
            for c in range(0,len(self.board[0])):
                print('cols',len(self.board[0]))
                if self.board[r,c]!=' ':
                    c+=1
        print(c)
        return c==self.rows*self.cols

    
    #Row-wise Match check
    def across_check(self,player):
        for i in range(0,self.board.shape[0]):#row
            c=0
            for j in range(0,self.board.shape[1]):#column
                if j<self.board.shape[1]-1: #should be 1 less than no.of cols
                    if self.board[i,j] == player and self.board[i,j+1] == player:
                        c+=1
            if c==self.board.shape[1]-1:
                print('Player {p} wins'.format(p=player))
                return True
            else:
                continue
    
    # Column-wise Match check
    def below_check(self,player):
        for i in range(0,self.board.shape[1]):#column
            d=0
            for j in range(0,self.board.shape[0]):#row
                if j<self.board.shape[0]-1: #4-1=3
                    if self.board[j,i]==player and self.board[j+1,i]==player:#2=3
                        d+=1
            if d==self.board.shape[0]-1:
                print('Player {p} wins!'.format(p=player))
                return True    
            else:
                continue

    # Diagonal Match check
    def diagonal_check(self,player): # Update for any dimension game
        if self.board[0,0]==player and self.board[1,1]==player and self.board[2,2]==player:
            print('Player {p} wins!'.format(p=player))
            return True
        if self.board[0,2]==player and self.board[1,1]==player and self.board[2,0]==player:
            print('Player {p} wins!'.format(p=player))
            return True
    
      
tk = TictacToe()
print(tk.start_game())

    