import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def game_2048():
    import random
    import os
    
    class Game2048:
        def __init__(self, size=4):
            self.size = size
            self.board = [[0 for _ in range(size)] for _ in range(size)]
            self.score = 0
            self.add_random_tile()
            self.add_random_tile()
        
        def add_random_tile(self):
            empty_cells = []
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == 0:
                        empty_cells.append((i, j))
            
            if empty_cells:
                i, j = random.choice(empty_cells)
                self.board[i][j] = 2 if random.random() < 0.9 else 4
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🧠 2048 🧠")
            print(f"Score: {self.score}")
            print("=" * (self.size * 6 + 1))
            
            for row in self.board:
                print("|", end="")
                for cell in row:
                    if cell == 0:
                        print("     |", end="")
                    else:
                        print(f" {cell:4} |", end="")
                print()
                print("=" * (self.size * 6 + 1))
            
            print("\nControls: W/A/S/D to move, R to restart, Q to quit")
            print("Join numbers to get to 2048!")
        
        def move(self, direction):
            # direction: 0=up, 1=right, 2=down, 3=left
            moved = False
            
            # Transpose or reverse based on direction
            if direction == 0:  # Up
                board = [list(row) for row in zip(*self.board)]
            elif direction == 1:  # Right
                board = [row[::-1] for row in self.board]
            elif direction == 2:  # Down
                board = [list(row) for row in zip(*self.board)]
                board = [row[::-1] for row in board]
            else:  # Left
                board = [row[:] for row in self.board]
            
            # Move and merge tiles
            for i in range(self.size):
                # Remove zeros
                new_row = [x for x in board[i] if x != 0]
                
                # Merge adjacent equal numbers
                j = 0
                while j < len(new_row) - 1:
                    if new_row[j] == new_row[j + 1]:
                        new_row[j] *= 2
                        self.score += new_row[j]
                        del new_row[j + 1]
                    j += 1
                
                # Pad with zeros
                new_row += [0] * (self.size - len(new_row))
                
                if board[i] != new_row:
                    moved = True
                board[i] = new_row
            
            # Convert back to original orientation
            if direction == 0:  # Up
                board = [list(row) for row in zip(*board)]
                self.board = board
            elif direction == 1:  # Right
                self.board = [row[::-1] for row in board]
            elif direction == 2:  # Down
                board = [row[::-1] for row in board]
                self.board = [list(row) for row in zip(*board)]
            else:  # Left
                self.board = board
            
            if moved:
                self.add_random_tile()
            
            return moved
        
        def check_game_over(self):
            # Check for empty cells
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == 0:
                        return False
            
            # Check for possible merges
            for i in range(self.size):
                for j in range(self.size):
                    current = self.board[i][j]
                    if (j < self.size - 1 and current == self.board[i][j + 1]) or \
                       (i < self.size - 1 and current == self.board[i + 1][j]):
                        return False
            
            return True
        
        def check_win(self):
            for row in self.board:
                if 2048 in row:
                    return True
            return False
    
    print("🧠 2048 Game 🧠")
    print("=" * 40)
    print("Combine tiles with the same number!")
    print("Use W/A/S/D keys to move tiles")
    input("\nPress Enter to start...")
    
    game = Game2048()
    
    while True:
        game.draw()
        
        if game.check_win():
            print("\n🎉 YOU WIN! You reached 2048!")
            choice = input("Continue playing? (y/n): ").lower()
            if choice != 'y':
                break
        
        if game.check_game_over():
            print("\n💀 GAME OVER! No more moves!")
            choice = input("Restart? (y/n): ").lower()
            if choice == 'y':
                game = Game2048()
                continue
            else:
                break
        
        key = input("\nMove (W/A/S/D/R/Q): ").lower()
        
        if key == 'q':
            break
        elif key == 'r':
            game = Game2048()
            continue
        
        moved = False
        if key == 'w':
            moved = game.move(0)
        elif key == 'd':
            moved = game.move(1)
        elif key == 's':
            moved = game.move(2)
        elif key == 'a':
            moved = game.move(3)
        
        if not moved:
            print("Invalid move or no movement!")
            input("Press Enter to continue...")

# 40. 🟩 Wordle Game

if __name__ == "__main__":
    game_2048()
