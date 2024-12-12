def is_valid_chess_board(board):
    for space in board.keys():
        if len(space) != 2:
            return False
        if space[0] < "1" or space[0] > "8":
            return False
        if space[1] < "a" or space[1] > "h":
            return False
        
        counter = {}
        for piece in board.values():
            if len(piece) < 2:
                return False
            player = piece[0]
            if player != "w" and player != "b":
                return False
            counter.setdefault(player, 0)
            counter[player] += 1

            if piece[1:] not in ("pawn", "knight", "bishop", "rook", "queen", "king"):
                return False
            counter.setdefault(piece, 0)
            counter[piece] += 1

        for player in ("w", "b"):
            if counter.get(player + "king", 0) != 1:
                return False
            if counter.get(player, 0) > 16:
                return False
            if counter.get(player + "pawn", 0) > 8:
                return False
            if counter.get(player + "knight", 0) > 2:
                return False
            if counter.get(player + "bishop", 0) > 2:
                return False
            if counter.get(player + "rock", 0) > 2:
                return False
            if counter.get(player + "queen", 0) > 1:
                return False
            
        return True
    
chess_board = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}
print(is_valid_chess_board(chess_board))