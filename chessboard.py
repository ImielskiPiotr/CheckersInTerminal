letters = ' abcdefgh'
board_row = '        '
board = [letters] + [board_row for x in range(8)]
start_positons = ['x x x x ', ' x x x x', 'o o o o ', ' o o o o']
for x in (8,6): board[x] = start_positons[0]
board[7] = start_positons[1]
for x in (1,3): board[x] = start_positons[3]
board[2] = start_positons[2] 
for x in range(1,9): board[x] = ' ' + board[x] + ' ' + str(x)



