def is_in_check(board):
    if not board or not all(len(row) == len(board) for row in board):
        return 
    
    size = len(board)
    pieces = {"K", "Q", "R", "B", "P"} 
    king_pos = None
    
    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                king_pos = (r, c)
                break
        if king_pos:
            break
    
    if not king_pos:
        return  
    
    kr, kc = king_pos  
    
    def check_diagonal():
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                if board[r][c] in pieces:
                    if board[r][c] in {"B", "Q"}:
                        return True
                    break
                r += dr
                c += dc
        return False
    
    def check_straight():
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                if board[r][c] in pieces:
                    if board[r][c] in {"R", "Q"}:
                        return True
                    break
                r += dr
                c += dc
        return False
    
    def check_pawn():
        for dr, dc in [(-1, -1), (-1, 1)]:
            r, c = kr + dr, kc + dc
            if 0 <= r < size and 0 <= c < size and board[r][c] == "P":
                return True
        return False
    
    if check_diagonal() or check_straight() or check_pawn():
        print("KING อยู่ในอันตราย")
    else:
        print("KING ปลอดภัย")


board = [
    [".", ".", ".", ".", "Q", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "B", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "K", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]

is_in_check(board)
