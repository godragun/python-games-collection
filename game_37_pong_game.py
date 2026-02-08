import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def pong_game():
    import random
    import time
    import os
    
    class Pong:
        def __init__(self, width=40, height=20):
            self.width = width
            self.height = height
            self.reset()
        
        def reset(self):
            self.player1_y = self.height // 2
            self.player2_y = self.height // 2
            self.ball_x = self.width // 2
            self.ball_y = self.height // 2
            self.ball_dx = random.choice([-1, 1])
            self.ball_dy = random.choice([-1, 1])
            self.score1 = 0
            self.score2 = 0
            self.paddle_height = 3
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🏓 PONG 🏓")
            print(f"Player 1: {self.score1}  Player 2: {self.score2}")
            print("=" * (self.width + 2))
            
            for y in range(self.height):
                line = "|"
                for x in range(self.width):
                    # Draw player 1 paddle
                    if x == 0 and abs(y - self.player1_y) <= self.paddle_height // 2:
                        line += "█"
                    # Draw player 2 paddle
                    elif x == self.width - 1 and abs(y - self.player2_y) <= self.paddle_height // 2:
                        line += "█"
                    # Draw ball
                    elif x == self.ball_x and y == self.ball_y:
                        line += "●"
                    else:
                        line += " "
                line += "|"
                print(line)
            
            print("=" * (self.width + 2))
            print("Player 1: W/S  Player 2: ↑/↓  Q to quit")
        
        def update(self, p1_up=False, p1_down=False, p2_up=False, p2_down=False):
            # Move paddles
            if p1_up and self.player1_y > self.paddle_height // 2:
                self.player1_y -= 1
            if p1_down and self.player1_y < self.height - self.paddle_height // 2 - 1:
                self.player1_y += 1
            if p2_up and self.player2_y > self.paddle_height // 2:
                self.player2_y -= 1
            if p2_down and self.player2_y < self.height - self.paddle_height // 2 - 1:
                self.player2_y += 1
            
            # Move ball
            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy
            
            # Ball collision with top/bottom
            if self.ball_y <= 0 or self.ball_y >= self.height - 1:
                self.ball_dy *= -1
            
            # Ball collision with paddles
            if self.ball_x == 1:
                if abs(self.ball_y - self.player1_y) <= self.paddle_height // 2:
                    self.ball_dx *= -1
                else:
                    self.score2 += 1
                    self.reset()
            
            if self.ball_x == self.width - 2:
                if abs(self.ball_y - self.player2_y) <= self.paddle_height // 2:
                    self.ball_dx *= -1
                else:
                    self.score1 += 1
                    self.reset()
    
    print("🏓 Pong Game 🏓")
    print("=" * 40)
    print("Player 1: W/S keys")
    print("Player 2: Up/Down arrow keys")
    print("First to 5 points wins!")
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
    
    game = Pong()
    
    try:
        while game.score1 < 5 and game.score2 < 5:
            game.draw()
            
            # Get key input
            key = get_key()
            p1_up = key == 'w' or key == 'W'
            p1_down = key == 's' or key == 'S'
            p2_up = key == '\x1b'  # Escape sequence for arrow keys
            p2_down = False
            
            if key == '\x1b':
                # Check for arrow keys
                next1 = get_key()
                next2 = get_key()
                if next1 == '[':
                    if next2 == 'A':
                        p2_up = True
                    elif next2 == 'B':
                        p2_down = True
            
            if key == 'q' or key == 'Q':
                break
            
            game.update(p1_up, p1_down, p2_up, p2_down)
            time.sleep(0.1)
        
        game.draw()
        if game.score1 >= 5:
            print("\n🎉 Player 1 wins!")
        elif game.score2 >= 5:
            print("\n🎉 Player 2 wins!")
        else:
            print("\nGame quit")
    
    except Exception as e:
        print(f"\nError: {e}")

# 38. 👾 Space Invaders (terminal version)


if __name__ == "__main__":
    pong_game()
