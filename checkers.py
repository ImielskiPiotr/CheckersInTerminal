from chessboard import board
from functions import jump, move, change_player, correct_type, winner, move_possibility

print( " \nRules: no obligatory and multiple jumps.\nWin when last line taken or opponent blocked.\nPlayer 'o' starts.\nType pawn's coordinates and decide, if not move is obligatory.\nCoordinates examples: a1, h8.\n ")

for x in board: print(x)

player = 'o'
game = 'on'

coordinates = correct_type(board, player, input("Player 'o' type coordinates: "))

while game != 'over':
     
    int_coordinates = [' abcdefgh'.index(coordinates[0]), int(coordinates[1])]

    y = int_coordinates[1]
    x = int_coordinates[0]

    board = jump(y,x,board,player)

    board = move(y,x,board,player)

    for x in board: print(x)

    game = winner(board, player, game)

    game = move_possibility(board, player, game)

    if game == 'over': break

    player = change_player(player)

    coordinates = correct_type(board, player, input())

    



    







    

     

 










    

    













