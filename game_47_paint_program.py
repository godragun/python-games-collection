import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def paint_program():
    import os
    
    class Paint:
        def __init__(self, width=20, height=20):
            self.width = width
            self.height = height
            self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
            self.cursor_x = width // 2
            self.cursor_y = height // 2
            self.color = '█'
            self.colors = {
                '1': '█',  # Block
                '2': '▓',  # Dark
                '3': '▒',  # Medium
                '4': '░',  # Light
                '5': '▄',  # Half top
                '6': '▀',  # Half bottom
                '7': '■',  # Square
                '8': '○',  # Circle
                '9': '✱',  # Star
                '0': '·'   # Dot
            }
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🎨 Terminal Paint 🎨")
            print("=" * (self.width + 4))
            
            for y in range(self.height):
                line = "│"
                for x in range(self.width):
                    if x == self.cursor_x and y == self.cursor_y:
                        line += "✏️"
                    else:
                        line += self.canvas[y][x]
                line += "│"
                print(line)
            
            print("=" * (self.width + 4))
            print(f"\nCursor: ({self.cursor_x}, {self.cursor_y})")
            print(f"Brush: {self.color}")
            print("\nControls:")
            print("WASD = Move cursor")
            print("Space = Draw")
            print("C = Clear canvas")
            print("1-0 = Change brush")
            print("Q = Quit")
            print("\nAvailable brushes:")
            for key, char in self.colors.items():
                print(f"{key}: {char}", end="  ")
            print()
        
        def move(self, dx, dy):
            self.cursor_x = max(0, min(self.width - 1, self.cursor_x + dx))
            self.cursor_y = max(0, min(self.height - 1, self.cursor_y + dy))
        
        def draw_at_cursor(self):
            self.canvas[self.cursor_y][self.cursor_x] = self.color
        
        def clear(self):
            self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
    
    print("🎨 Paint Program 🎨")
    print("=" * 40)
    print("Draw in the terminal!")
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
    
    paint = Paint(width=30, height=15)
    
    while True:
        paint.draw()
        
        key = get_key()
        
        if key == 'q' or key == 'Q':
            break
        elif key == 'w' or key == 'W':
            paint.move(0, -1)
        elif key == 's' or key == 'S':
            paint.move(0, 1)
        elif key == 'a' or key == 'A':
            paint.move(-1, 0)
        elif key == 'd' or key == 'D':
            paint.move(1, 0)
        elif key == ' ':
            paint.draw_at_cursor()
        elif key == 'c' or key == 'C':
            paint.clear()
        elif key in paint.colors:
            paint.color = paint.colors[key]
    
    print("\n🎨 Your masterpiece has been saved!")
    
    # Save to file
    with open("drawing.txt", "w") as f:
        f.write("Terminal Drawing:\n")
        f.write("=" * (paint.width + 4) + "\n")
        for row in paint.canvas:
            f.write("│" + "".join(row) + "│\n")
        f.write("=" * (paint.width + 4) + "\n")
    
    print("Saved to 'drawing.txt'")

# 48. 🚢 Battleship (already done as #34, so here's enhanced version)


if __name__ == "__main__":
    paint_program()
