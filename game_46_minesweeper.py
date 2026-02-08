import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def minesweeper():
    import random
    
    class Minesweeper:
        def __init__(self, size=8, mines=10):
            self.size = size
            self.mines = mines
            self.board = [[0 for _ in range(size)] for _ in range(size)]
            self.revealed = [[False for _ in range(size)] for _ in range(size)]
            self.flagged = [[False for _ in range(size)] for _ in range(size)]
            self.game_over = False
            self.win = False
            self.first_click = True
            self.generate_board()
        
        def generate_board(self, safe_x=None, safe_y=None):
            # Place mines
            mines_placed = 0
            while mines_placed < self.mines:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                
                # Ensure first click is safe
                if self.first_click and safe_x is not None and safe_y is not None:
                    if abs(x - safe_x) <= 1 and abs(y - safe_y) <= 1:
                        continue
                
                if self.board[y][x] != -1:
                    self.board[y][x] = -1
                    mines_placed += 1
            
            # Calculate numbers
            for y in range(self.size):
                for x in range(self.size):
                    if self.board[y][x] != -1:
                        count = 0
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if dy == 0 and dx == 0:
                                    continue
                                ny, nx = y + dy, x + dx
                                if 0 <= ny < self.size and 0 <= nx < self.size:
                                    if self.board[ny][nx] == -1:
                                        count += 1
                        self.board[y][x] = count
        
        def reveal(self, x, y):
            if self.first_click:
                self.first_click = False
                self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
                self.generate_board(x, y)
                return self.reveal(x, y)
            
            if not (0 <= x < self.size and 0 <= y < self.size):
                return
            
            if self.revealed[y][x] or self.flagged[y][x]:
                return
            
            self.revealed[y][x] = True
            
            if self.board[y][x] == -1:
                self.game_over = True
                return
            
            # Reveal adjacent cells if this cell is 0
            if self.board[y][x] == 0:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.size and 0 <= nx < self.size:
                            if not self.revealed[ny][nx] and not self.flagged[ny][nx]:
                                self.reveal(nx, ny)
        
        def toggle_flag(self, x, y):
            if not self.revealed[y][x]:
                self.flagged[y][x] = not self.flagged[y][x]
        
        def check_win(self):
            for y in range(self.size):
                for x in range(self.size):
                    if self.board[y][x] != -1 and not self.revealed[y][x]:
                        return False
            self.win = True
            return True
        
        def draw(self):
            print("💣 MINESWEEPER 💣")
            print(f"Mines: {self.mines}")
            print("=" * (self.size * 2 + 3))
            
            # Column numbers
            print("  " + " ".join(str(i) for i in range(self.size)))
            print(" +" + "-" * (self.size * 2) + "+")
            
            for y in range(self.size):
                row = f"{y}|"
                for x in range(self.size):
                    if self.game_over and self.board[y][x] == -1:
                        row += "💣"
                    elif self.flagged[y][x]:
                        row += "🚩"
                    elif not self.revealed[y][x]:
                        row += "■"
                    else:
                        if self.board[y][x] == 0:
                            row += " "
                        else:
                            # Colored numbers
                            colors = ['', '\033[94m', '\033[92m', '\033[91m', '\033[95m',
                                     '\033[93m', '\033[96m', '\033[90m', '\033[97m']
                            num = self.board[y][x]
                            if num == -1:
                                row += "💣"
                            else:
                                row += f"{colors[num]}{num}\033[0m"
                        row += " "
                row += "|"
                print(row)
            
            print(" +" + "-" * (self.size * 2) + "+")
            
            if self.game_over:
                if self.win:
                    print("\n🎉 YOU WIN! All mines found!")
                else:
                    print("\n💥 GAME OVER! You hit a mine!")
            else:
                print("\nCommands: R X Y = Reveal, F X Y = Flag, Q = Quit")
                print("Example: 'R 3 4' reveals cell at (3,4)")
    
    print("💣 Minesweeper 💣")
    print("=" * 40)
    print("Find all mines without triggering them!")
    print("Use flags to mark suspected mines")
    
    game = Minesweeper(size=8, mines=10)
    
    while not game.game_over and not game.win:
        game.draw()
        
        cmd = input("\n> ").strip().upper()
        
        if cmd == 'Q':
            break
        
        if len(cmd.split()) == 3:
            action, x_str, y_str = cmd.split()
            
            try:
                x = int(x_str)
                y = int(y_str)
                
                if 0 <= x < game.size and 0 <= y < game.size:
                    if action == 'R':
                        game.reveal(x, y)
                        if not game.game_over:
                            game.check_win()
                    elif action == 'F':
                        game.toggle_flag(x, y)
                        game.check_win()
                    else:
                        print("Invalid action. Use R or F")
                else:
                    print(f"Coordinates must be 0-{game.size-1}")
            except ValueError:
                print("Invalid coordinates")
        else:
            print("Invalid command format. Use: R X Y or F X Y")
    
    game.draw()

# 47. 🎨 Paint (simple terminal drawing)


if __name__ == "__main__":
    minesweeper()
