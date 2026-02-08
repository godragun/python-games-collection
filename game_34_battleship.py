import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def battleship():
    import random
    
    BOARD_SIZE = 5
    SHIP_SIZES = [3, 2, 2]
    
    def create_board():
        return [['~' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    def place_ships(board, ships):
        for size in ships:
            placed = False
            while not placed:
                horizontal = random.choice([True, False])
                if horizontal:
                    row = random.randint(0, BOARD_SIZE - 1)
                    col = random.randint(0, BOARD_SIZE - size)
                else:
                    row = random.randint(0, BOARD_SIZE - size)
                    col = random.randint(0, BOARD_SIZE - 1)
                
                # Check if space is available
                available = True
                if horizontal:
                    for i in range(size):
                        if board[row][col + i] != '~':
                            available = False
                            break
                else:
                    for i in range(size):
                        if board[row + i][col] != '~':
                            available = False
                            break
                
                if available:
                    if horizontal:
                        for i in range(size):
                            board[row][col + i] = 'S'
                    else:
                        for i in range(size):
                            board[row + i][col] = 'S'
                    placed = True
    
    def print_board(board, show_ships=False):
        print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
        for i in range(BOARD_SIZE):
            row_display = []
            for j in range(BOARD_SIZE):
                if board[i][j] == 'S' and not show_ships:
                    row_display.append('~')
                else:
                    row_display.append(board[i][j])
            print(f"{i} " + " ".join(row_display))
    
    print("🚢 Battleship 🚢")
    print("=" * 40)
    print("\nTry to sink all 3 ships!")
    print("Sizes: 3, 2, and 2 spaces")
    
    board = create_board()
    player_board = create_board()
    place_ships(board, SHIP_SIZES)
    
    ships_remaining = sum(SHIP_SIZES)
    shots = 0
    
    while ships_remaining > 0:
        print("\nYour board:")
        print_board(player_board)
        
        try:
            row = int(input(f"\nRow (0-{BOARD_SIZE-1}): "))
            col = int(input(f"Col (0-{BOARD_SIZE-1}): "))
            
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print("Invalid coordinates!")
                continue
            
            if player_board[row][col] != '~':
                print("You already shot there!")
                continue
            
            shots += 1
            
            if board[row][col] == 'S':
                print("💥 Hit!")
                player_board[row][col] = 'X'
                board[row][col] = 'X'
                ships_remaining -= 1
            else:
                print("💦 Miss!")
                player_board[row][col] = 'O'
            
            print(f"Ships remaining: {ships_remaining}")
            
        except ValueError:
            print("Please enter numbers")
    
    print(f"\n🎉 You sank all ships in {shots} shots!")

# 35. 🔴 Connect Four

if __name__ == "__main__":
    battleship()
