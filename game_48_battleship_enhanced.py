import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def battleship_enhanced():
    import random
    
    class BattleshipEnhanced:
        def __init__(self):
            self.size = 8
            self.ships = {
                'Carrier': 5,
                'Battleship': 4,
                'Cruiser': 3,
                'Submarine': 3,
                'Destroyer': 2
            }
            self.player_board = self.create_board()
            self.computer_board = self.create_board()
            self.player_target = self.create_board()
            self.place_ships(self.player_board, True)
            self.place_ships(self.computer_board, False)
            self.player_turn = True
        
        def create_board(self):
            return [['~' for _ in range(self.size)] for _ in range(self.size)]
        
        def place_ships(self, board, is_player):
            for ship, length in self.ships.items():
                placed = False
                while not placed:
                    horizontal = random.choice([True, False])
                    if horizontal:
                        row = random.randint(0, self.size - 1)
                        col = random.randint(0, self.size - length)
                    else:
                        row = random.randint(0, self.size - length)
                        col = random.randint(0, self.size - 1)
                    
                    # Check if space is available
                    available = True
                    if horizontal:
                        for i in range(length):
                            if board[row][col + i] != '~':
                                available = False
                                break
                    else:
                        for i in range(length):
                            if board[row + i][col] != '~':
                                available = False
                                break
                    
                    if available:
                        if horizontal:
                            for i in range(length):
                                board[row][col + i] = ship[0]
                        else:
                            for i in range(length):
                                board[row + i][col] = ship[0]
                        
                        if is_player:
                            print(f"Placed {ship} ({length} spaces)")
                        placed = True
        
        def draw_boards(self):
            print("\nYour Fleet:".ljust(25) + "Enemy Waters:")
            print(" " + " ".join(str(i) for i in range(self.size)) + " " * 5 + " " + " ".join(str(i) for i in range(self.size)))
            
            for y in range(self.size):
                # Player board
                player_line = f"{y}|"
                for x in range(self.size):
                    cell = self.player_board[y][x]
                    if cell == '~':
                        player_line += "~"
                    elif cell == 'X':
                        player_line += "💥"
                    elif cell == 'O':
                        player_line += "💦"
                    else:
                        player_line += cell
                    player_line += " "
                
                # Target board
                target_line = f"{y}|"
                for x in range(self.size):
                    cell = self.player_target[y][x]
                    if cell == 'X':
                        target_line += "💥"
                    elif cell == 'O':
                        target_line += "💦"
                    else:
                        target_line += "~"
                    target_line += " "
                
                print(player_line + " " * 3 + target_line)
        
        def player_shot(self):
            print("\nYour turn!")
            while True:
                try:
                    x = int(input("Enter X coordinate (0-7): "))
                    y = int(input("Enter Y coordinate (0-7): "))
                    
                    if not (0 <= x < self.size and 0 <= y < self.size):
                        print("Coordinates out of range!")
                        continue
                    
                    if self.player_target[y][x] != '~':
                        print("You already shot there!")
                        continue
                    
                    # Check hit
                    if self.computer_board[y][x] != '~':
                        print("💥 HIT!")
                        self.player_target[y][x] = 'X'
                        self.computer_board[y][x] = 'X'
                        return True
                    else:
                        print("💦 MISS!")
                        self.player_target[y][x] = 'O'
                        return False
                        
                except ValueError:
                    print("Please enter numbers!")
        
        def computer_shot(self):
            print("\nComputer's turn...")
            import time
            time.sleep(1)
            
            # Simple AI: random shots
            while True:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                
                if self.player_board[y][x] not in ['X', 'O']:
                    if self.player_board[y][x] != '~':
                        print(f"Computer hits at ({x},{y})!")
                        self.player_board[y][x] = 'X'
                        return True
                    else:
                        print(f"Computer misses at ({x},{y})")
                        self.player_board[y][x] = 'O'
                        return False
        
        def check_game_over(self):
            # Check if all ships sunk on either board
            player_ships = sum(1 for row in self.player_board for cell in row if cell.isalpha())
            computer_ships = sum(1 for row in self.computer_board for cell in row if cell.isalpha())
            
            if player_ships == 0:
                return "computer"
            if computer_ships == 0:
                return "player"
            return None
    
    print("🚢 Enhanced Battleship 🚢")
    print("=" * 40)
    print("Ships: Carrier(5), Battleship(4), Cruiser(3), Submarine(3), Destroyer(2)")
    
    game = BattleshipEnhanced()
    
    while True:
        game.draw_boards()
        
        if game.player_turn:
            hit = game.player_shot()
            if not hit:
                game.player_turn = False
        else:
            hit = game.computer_shot()
            if not hit:
                game.player_turn = True
        
        winner = game.check_game_over()
        if winner:
            game.draw_boards()
            if winner == "player":
                print("\n🎉 YOU WIN! All enemy ships sunk!")
            else:
                print("\n💻 COMPUTER WINS! Your fleet is destroyed!")
            break
        
        input("\nPress Enter to continue...")



if __name__ == "__main__":
    battleship_enhanced()
