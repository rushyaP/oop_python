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
       list_view=[[board[i,j] for j in range(board.shape[1])] for i in range(board.shape[0])]
       for row in list_view:
            print("|".join(row))
            print("-"*5)

    def play_game(self):
        print('play func begining')
        while True:
            x_choice=list(input("\nX) Where do you want to mark your position? Enter row and column number in xy format"))
            self.update_board(x_choice,'X')
            self.display_board(self.board)
            if self.match_check('X'):
                play_again = input("Do you want to play again? Give Y/N")
                if play_again.upper()=='Y':
                    self.start_game()
                else:
                    print('Hope you have enjoyed the game')
                    break
                    
            o_choice=list(input("\nO) Where do you want to mark your position? Enter row and column number in xy format"))
            self.update_board(o_choice,'O')
            self.display_board(self.board)
            if self.match_check('O'):
                play_again = input("Do you want to play again? Give Y/N")
                if play_again.upper()=='Y':
                    self.start_game()
                else:
                    print('Hope you have enjoyed the game')
                    break
            

    def update_board(self,player_choice,player):
        if self.board[int(player_choice[0])-1,int(player_choice[1])-1]==' ':
            self.board[int(player_choice[0])-1,int(player_choice[1])-1] = player
        else:
            print('This position is taken. Please give another position')

    def match_check(self,player):
        if self.diagonal_check(player) or self.across_check(player) or self.below_check(player):
            return True
        else:
            return False
        
    def match_tie_check(self):
        pass
    
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
                return True
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

    