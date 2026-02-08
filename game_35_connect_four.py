import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def connect_four():
    ROWS = 6
    COLS = 7
    
    def create_board():
        return [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    
    def print_board(board):
        print("\n" + "=" * 29)
        for row in board:
            print("| " + " | ".join(row) + " |")
            print("=" * 29)
        print("  " + "   ".join(str(i) for i in range(COLS)))
    
    def drop_piece(board, col, piece):
        for row in range(ROWS-1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = piece
                return row
        return -1  # Column is full
    
    def check_winner(board, row, col, piece):
        # Check horizontal
        for c in range(COLS - 3):
            if all(board[row][c + i] == piece for i in range(4)):
                return True
        
        # Check vertical
        for r in range(ROWS - 3):
            if all(board[r + i][col] == piece for i in range(4)):
                return True
        
        # Check diagonal (down-right)
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(board[r + i][c + i] == piece for i in range(4)):
                    return True
        
        # Check diagonal (up-right)
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(board[r - i][c + i] == piece for i in range(4)):
                    return True
        
        return False
    
    print("🔴 Connect Four 🟡")
    print("=" * 40)
    
    board = create_board()
    current_player = '🔴'
    
    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        try:
            col = int(input(f"Choose column (0-{COLS-1}): "))
            
            if col < 0 or col >= COLS:
                print("Invalid column!")
                continue
            
            row = drop_piece(board, col, current_player)
            if row == -1:
                print("Column is full!")
                continue
            
            if check_winner(board, row, col, current_player):
                print_board(board)
                print(f"\n🎉 Player {current_player} wins!")
                break
            
            # Check for tie
            if all(board[0][c] != ' ' for c in range(COLS)):
                print_board(board)
                print("\n🤝 It's a tie!")
                break
            
            current_player = '🟡' if current_player == '🔴' else '🔴'
            
        except ValueError:
            print("Please enter a number")



if __name__ == "__main__":
    connect_four()
