def move(y, x, board, player):

    turn = 1 if 'o' in player else -1
    
    if board[y][x] is player[0]:

        if x == 1 and board[y+1*turn][x+1] == ' ':
            board[y] = board[y][:x] + ' ' + board[y][x+1:]
            board[y+1*turn] = board[y+1*turn][:x+1] + player[0] + board[y+1*turn][x+2:]

        elif x == 8 and board[y+1*turn][x-1] == ' ':
            board[y] = board[y][:x] + ' ' + board[y][x+1:]
            board[y+1*turn] = board[y+1*turn][:x-1] + player[0] + board[y+1*turn][x:]  

        elif x in (2,3,4,5,6,7):
            if ' ' == board[y+1*turn][x+1] and ' ' == board[y+1*turn][x-1]:
                 
                question = input("Left 'l' or right 'r': ")
                while len(question) < 1 or question[0] not in ('l','r'):
                    question = input("Left 'l' or right 'r': ")

                board[y] = board[y][:x] + ' ' + board[y][x+1:]

                if question == 'l':
                    board[y+1*turn] = board[y+1*turn][:x-1] + player[0] + board[y+1*turn][x:]
                else: board[y+1*turn] = board[y+1*turn][:x+1] + player[0] + board[y+1*turn][x+2:]
                
            else: 
                if ' ' == board[y+1*turn][x+1]:
                    board[y] = board[y][:x] + ' ' + board[y][x+1:]
                    board[y+1*turn] = board[y+1*turn][:x+1] + player[0] + board[y+1*turn][x+2:]
                elif ' ' == board[y+1*turn][x-1]:
                    board[y] = board[y][:x] + ' ' + board[y][x+1:]
                    board[y+1*turn] = board[y+1*turn][:x-1] + player[0] + board[y+1*turn][x:]    

    return board


def jump(y, x, board, player): 

    turn = 1 if 'o' in player else -1
    
    if y not in ((1,2) if player == 'x' else (7,8)):

        if x in (1,2) and board[y+1*turn][x+1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x+2] == ' ':
            board[y] = board[y][:x] + ' ' + board[y][x+1:]
            board[y+1*turn] = board[y+1*turn][:x+1] + ' ' + board[y+1*turn][x+2:]
            board[y+2*turn] = board[y+2*turn][:x+2] + player[0] + board[y+2*turn][x+3:]

        elif x in (7,8) and board[y+1*turn][x-1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x-2] == ' ':
            board[y] = board[y][:x] + ' ' + board[y][x+1:]
            board[y+1*turn] = board[y+1*turn][:x-1] + ' ' + board[y+1*turn][x:]
            board[y+2*turn] = board[y+2*turn][:x-2] + player[0] + board[y+2*turn][x-1:]  
     
        elif x in (3,4,5,6):
            if (('o' if player == 'x' else 'x') == board[y+1*turn][x+1] and ('o' if player == 'x' else 'x') == board[y+1*turn][x-1] and
                board[y+2*turn][x+2] == ' ' and board[y+2*turn][x-2] == ' '):
                 
                question = input("Left 'l' or right 'r': ")
                while len(question) < 1 or question[0] not in ('l','r'):
                    question = input("Left 'l' or right 'r': ")

                board[y] = board[y][:x] + ' ' + board[y][x+1:]

                if question == 'l':
                    board[y+1*turn] = board[y+1*turn][:x-1] + ' ' + board[y+1*turn][x:]
                    board[y+2*turn] = board[y+2*turn][:x-2] + player[0] + board[y+2*turn][x-1:]
                else: 
                    board[y+1*turn] = board[y+1*turn][:x+1] + ' ' + board[y+1*turn][x+2:]
                    board[y+2*turn] = board[y+2*turn][:x+2] + player[0] + board[y+2*turn][x+3:]
                
            else: 
                if ('o' if player == 'x' else 'x') == board[y+1*turn][x+1] and board[y+2*turn][x+2] == ' ':
                    board[y] = board[y][:x] + ' ' + board[y][x+1:]
                    board[y+1*turn] = board[y+1*turn][:x+1] + ' ' + board[y+1*turn][x+2:]
                    board[y+2*turn] = board[y+2*turn][:x+2] + player[0] + board[y+2*turn][x+3:]
                elif ('o' if player == 'x' else 'x') == board[y+1*turn][x-1] and board[y+2*turn][x-2] == ' ':
                    board[y] = board[y][:x] + ' ' + board[y][x+1:]
                    board[y+1*turn] = board[y+1*turn][:x-1] + ' ' + board[y+1*turn][x:]  
                    board[y+2*turn] = board[y+2*turn][:x-2] + player[0] + board[y+2*turn][x-1:]
    return board


def winner(board, player, game):

    line = 1 if player == 'x' else 8
    
    if player in board[line]: 
        
        print("Last line conquered." + "'" + player + "'" + ' win!')    
        game = 'over'
    
    test = 0
    for a in range(1,9):   
    
        if ('o' if player == 'x' else 'x') not in board[a]:  

            test += 1
            
    if test == 8:

        print("Opponent conquered." + "'" + player + "'" + ' win!')    
        game = 'over'           

    return game


def change_player(player):

    if player == 'x': player = 'o'
    else: player ='x'

    if player == 'x': print("'x' turn: ")
    else: print("'o' turn: ")

    return player


def move_possibility(board, player, game):

    player = 'x' if player == 'o' else 'o'
    turn = 1 if 'o' == player else -1
    good_pawns = 0
    bad_pwans = 0
    
    for y in range(1,9):
        for x in range(1,9):
            
            good_pawns += 1            
             
            if (board[y][x] == player and
               ((x==1 and
                board[y+1*turn][x+1] != ' ' and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x+1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x+2] != ' ')) or
                (x == 2 and
                board[y+1*turn][x+1] != ' ' and
                board[y+1*turn][x-1] != ' ' and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x+1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x+2] != ' ')) or
                (x in (3,4,5,6)and
                board[y+1*turn][x+1] != ' ' and
                board[y+1*turn][x-1] != ' ' and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x+1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x+2] != ' ') and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x-1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x-2] != ' ')) or
                (x == 7 and
                board[y+1*turn][x+1] != ' ' and
                board[y+1*turn][x-1] != ' ' and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x-1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x-2] != ' ')) or
                (x == 8 and
                board[y+1*turn][x-1] != ' ' and
                ((y not in ((1,2) if player == 'x' else (7,8))) and
                board[y+1*turn][x-1] == ('o' if player == 'x' else 'x') and board[y+2*turn][x-2] != ' ')))):
   
                good_pawns += 1    

    if good_pawns == bad_pwans: 
        
        player = change_player(player)
        print("Last line conquered." + "'" + player + "'" + ' win!')
        game = 'over'

    return game


def correct_type(board, player, type): 

    while (len(type) < 2 or type[0] not in 'abcdefgh' or type[1] not in '12345678' or
            board[int(type[1])][' abcdefgh'.index(type[0])] != player):
        
        type = input('Wrong coordinates: ')

    int_coordinates = [' abcdefgh'.index(type[0]), int(type[1])]

    y = int_coordinates[1]
    x = int_coordinates[0]
    
    turn = 1 if 'o' == player else -1 

    while (((x==1 and
            board[y+1*turn][x+1] != ' ') and
            (x==1 and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x+1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x+2] != ' '))) or
           
           ((x==8 and
            board[y+1*turn][x-1] != ' ') and
            (x==8 and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x-1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x-2] != ' '))) or
           
           ((x == 2 and
            board[y+1*turn][x+1] != ' ' and
            board[y+1*turn][x-1] != ' ' ) and
            (x == 2 and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x+1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x+2] != ' '))) or
            
           ((x in (3,4,5,6) and
            board[y+1*turn][x+1] != ' ' and
            board[y+1*turn][x-1] != ' ') and
            (x in (3,4,5,6)) and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x+1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x+2] != ' ') and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x-1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x-2] != ' ')) or
            
            ((x == 7 and
            board[y+1*turn][x+1] != ' ' and
            board[y+1*turn][x-1] != ' ' ) and
            (x == 7 and
            ((y in ((1,2) if player == 'x' else (7,8))) or
            board[y+1*turn][x-1] != ('o' if player == 'x' else 'x') or board[y+2*turn][x-2] != ' ')))):   
   
        type = input("Pawn cannot move: ")

        while (len(type) < 2 or type[0] not in 'abcdefgh' or type[1] not in '12345678' or
            board[int(type[1])][' abcdefgh'.index(type[0])] != player):
        
            type = input('Wrong coordinates: ')

    

        int_coordinates = [' abcdefgh'.index(type[0]), int(type[1])]
        y = int_coordinates[1]
        x = int_coordinates[0]

    return type

        








             



