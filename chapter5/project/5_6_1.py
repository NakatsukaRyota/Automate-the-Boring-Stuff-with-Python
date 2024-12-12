chess_board = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}

board_key = []
board_value = []

for i in range(1, 9):
    for char in "abcdefgh":
        board_key.append(str(i) + char)
for i in "wb":
    for j in ["king", "pawn", "knight", "bishop", "rook", "queen"]:
        board_value.append(i + j)
        
print(board_key)
print(board_value)


def is_valid_chess_board(board):
    status = True
    for k in board.keys():
        if k not in board_key:
            status = False
        
    for v in board.values():
        if v not in board_value:
            status = False

    return status 

print(is_valid_chess_board(chess_board))