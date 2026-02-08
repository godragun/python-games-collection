import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    
    def print_board():
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")
    
    def check_winner():
        # Winning combinations
        wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
                (0,3,6), (1,4,7), (2,5,8),  # columns
                (0,4,8), (2,4,6)]           # diagonals
        
        for a, b, c in wins:
            if board[a] == board[b] == board[c] != ' ':
                return board[a]
        
        if ' ' not in board:
            return 'Tie'
        
        return None
    
    print("❌ Tic-Tac-Toe ⭕")
    print("=" * 40)
    print("\nPositions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
    while True:
        print_board()
        print(f"Player {current_player}'s turn")
        
        try:
            position = int(input("Enter position (1-9): ")) - 1
            
            if position < 0 or position > 8:
                print("Position must be 1-9")
                continue
            
            if board[position] != ' ':
                print("Position already taken!")
                continue
            
            board[position] = current_player
            
            winner = check_winner()
            if winner:
                print_board()
                if winner == 'Tie':
                    print("🤝 It's a tie!")
                else:
                    print(f"🎉 Player {winner} wins!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Please enter a number 1-9")

# 34. 🚢 Battleship

if __name__ == "__main__":
    tic_tac_toe()
