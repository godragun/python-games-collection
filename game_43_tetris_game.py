import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def tetris_game():
    import random
    import time
    import os
    
    # Tetromino shapes
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[1, 1, 1], [0, 1, 0]],  # T
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 0, 1]],  # J
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1, 0], [0, 1, 1]]   # Z
    ]
    
    COLORS = ['cyan', 'yellow', 'purple', 'orange', 'blue', 'green', 'red']
    
    class Tetris:
        def __init__(self, width=10, height=20):
            self.width = width
            self.height = height
            self.board = [[0 for _ in range(width)] for _ in range(height)]
            self.score = 0
            self.level = 1
            self.lines_cleared = 0
            self.game_over = False
            self.new_piece()
        
        def new_piece(self):
            self.piece_idx = random.randint(0, 6)
            self.piece = [row[:] for row in SHAPES[self.piece_idx]]
            self.piece_color = COLORS[self.piece_idx]
            self.piece_x = self.width // 2 - len(self.piece[0]) // 2
            self.piece_y = 0
            
            if self.check_collision():
                self.game_over = True
        
        def check_collision(self):
            for y, row in enumerate(self.piece):
                for x, cell in enumerate(row):
                    if cell:
                        board_x = self.piece_x + x
                        board_y = self.piece_y + y
                        
                        if (board_x < 0 or board_x >= self.width or
                            board_y >= self.height or
                            (board_y >= 0 and self.board[board_y][board_x])):
                            return True
            return False
        
        def merge_piece(self):
            for y, row in enumerate(self.piece):
                for x, cell in enumerate(row):
                    if cell:
                        board_x = self.piece_x + x
                        board_y = self.piece_y + y
                        if board_y >= 0:
                            self.board[board_y][board_x] = self.piece_color
        
        def clear_lines(self):
            lines_to_clear = []
            for y in range(self.height):
                if all(self.board[y]):
                    lines_to_clear.append(y)
            
            for line in lines_to_clear:
                del self.board[line]
                self.board.insert(0, [0 for _ in range(self.width)])
            
            cleared = len(lines_to_clear)
            if cleared > 0:
                self.lines_cleared += cleared
                self.score += [100, 300, 500, 800][min(cleared-1, 3)] * self.level
                self.level = self.lines_cleared // 10 + 1
        
        def rotate_piece(self):
            # Transpose and reverse rows for clockwise rotation
            rotated = [list(row) for row in zip(*self.piece[::-1])]
            old_piece = self.piece
            self.piece = rotated
            
            if self.check_collision():
                self.piece = old_piece
        
        def move(self, dx, dy):
            old_x, old_y = self.piece_x, self.piece_y
            self.piece_x += dx
            self.piece_y += dy
            
            if self.check_collision():
                self.piece_x, self.piece_y = old_x, old_y
                
                if dy > 0:  # Moving down caused collision
                    self.merge_piece()
                    self.clear_lines()
                    self.new_piece()
                return False
            
            return True
        
        def drop(self):
            while self.move(0, 1):
                pass
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🧱 TETRIS 🧱")
            print(f"Score: {self.score}  Level: {self.level}  Lines: {self.lines_cleared}")
            print("=" * (self.width * 2 + 2))
            
            # Create display board with current piece
            display_board = [row[:] for row in self.board]
            
            # Add current piece to display
            for y, row in enumerate(self.piece):
                for x, cell in enumerate(row):
                    if cell and self.piece_y + y >= 0:
                        display_board[self.piece_y + y][self.piece_x + x] = self.piece_color
            
            # Draw board
            for y in range(self.height):
                line = "|"
                for x in range(self.width):
                    cell = display_board[y][x]
                    if cell:
                        # Use colored blocks
                        color_codes = {
                            'cyan': '\033[96m█\033[0m',
                            'yellow': '\033[93m█\033[0m',
                            'purple': '\033[95m█\033[0m',
                            'orange': '\033[91m█\033[0m',
                            'blue': '\033[94m█\033[0m',
                            'green': '\033[92m█\033[0m',
                            'red': '\033[91m█\033[0m'
                        }
                        line += color_codes.get(cell, '█')
                    else:
                        line += " "
                    line += " "
                line = line.rstrip() + "|"
                print(line)
            
            print("=" * (self.width * 2 + 2))
            
            if self.game_over:
                print("\n💀 GAME OVER!")
                print(f"Final Score: {self.score}")
            
            print("\nControls: A/D=Left/Right, W=Rotate, S=Soft Drop")
            print("Space=Hard Drop, P=Pause, Q=Quit")
            print(f"Speed: {0.5/self.level:.1f}s per move")
    
    print("🧱 Tetris Game 🧱")
    print("=" * 40)
    print("Stack the blocks without reaching the top!")
    input("\nPress Enter to start...")
    
    import sys
    import tty
    import termios
    
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    game = Tetris()
    paused = False
    last_move = time.time()
    
    try:
        while not game.game_over:
            if not paused:
                game.draw()
                
                # Auto move down based on level
                current_time = time.time()
                if current_time - last_move > 0.5 / game.level:
                    game.move(0, 1)
                    last_move = current_time
            
            # Get input
            key = get_key()
            
            if key == 'q' or key == 'Q':
                break
            elif key == 'p' or key == 'P':
                paused = not paused
                if paused:
                    print("\n⏸️  PAUSED")
                else:
                    last_move = time.time()
            elif not paused:
                if key == 'a' or key == 'A':
                    game.move(-1, 0)
                elif key == 'd' or key == 'D':
                    game.move(1, 0)
                elif key == 's' or key == 'S':
                    game.move(0, 1)
                    last_move = time.time()
                elif key == 'w' or key == 'W':
                    game.rotate_piece()
                elif key == ' ':
                    game.drop()
                    last_move = time.time()
        
        game.draw()
        
    except Exception as e:
        print(f"\nError: {e}")

# 44-50. Additional games with simpler implementations

# 44. ◼️ Cards Against Humanity (simplified)


if __name__ == "__main__":
    tetris_game()
