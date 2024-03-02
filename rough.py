def is_valid(input_list):
    if input_list[0].isdigit() and input_list[-1].isdigit():
        return True
    else:
        print('Invalid input. Please give only numbers')
        return False
    
player_choice=input("{player}'s turn: Where do you want to mark your position? Enter row and column number in x,y format".format(player='X'))
print([int(i) for i in player_choice.split(',')])