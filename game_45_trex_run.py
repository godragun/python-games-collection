import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def trex_run():
    import random
    import time
    import os
    
    class TRexGame:
        def __init__(self, width=50):
            self.width = width
            self.trex_pos = 2
            self.ground_level = 10
            self.is_jumping = False
            self.jump_height = 0
            self.max_jump = 5
            self.obstacles = []
            self.score = 0
            self.game_speed = 0.2
            self.game_over = False
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🦖 T-REX RUN 🦖")
            print(f"Score: {self.score}")
            print("=" * (self.width + 2))
            
            for line in range(12):
                if line == self.ground_level:
                    # Ground line
                    ground_line = "█" * (self.width + 2)
                    print(ground_line)
                elif line == self.ground_level - self.trex_pos:
                    # T-Rex line
                    trex_line = " " * 2
                    if self.is_jumping:
                        trex_line += "🦖"
                    else:
                        trex_line += "🦖"
                    trex_line += " " * (self.width - 3)
                    print("|" + trex_line + "|")
                else:
                    # Empty line or obstacles
                    line_str = "|"
                    for col in range(self.width):
                        has_obstacle = False
                        for obs in self.obstacles:
                            if obs['x'] == col and obs['y'] == line:
                                line_str += "🌵"
                                has_obstacle = True
                                break
                        
                        if not has_obstacle:
                            if line == self.ground_level - 1:
                                line_str += "_"
                            else:
                                line_str += " "
                    line_str += "|"
                    print(line_str)
            
            print("=" * (self.width + 2))
            print("\nControls: Space = Jump, Q = Quit")
            
            if self.game_over:
                print("\n💥 GAME OVER!")
                print(f"Final Score: {self.score}")
        
        def update(self):
            # Update jump
            if self.is_jumping:
                self.trex_pos = self.jump_height
                self.jump_height -= 1
                if self.jump_height < 0:
                    self.is_jumping = False
                    self.trex_pos = 2
            
            # Move obstacles
            for obs in self.obstacles:
                obs['x'] -= 1
            
            # Remove off-screen obstacles
            self.obstacles = [obs for obs in self.obstacles if obs['x'] >= 0]
            
            # Add new obstacles
            if random.random() < 0.1:  # 10% chance each frame
                self.obstacles.append({
                    'x': self.width - 1,
                    'y': self.ground_level - 1,
                    'type': 'cactus'
                })
            
            # Check collisions
            for obs in self.obstacles:
                if obs['x'] == 2 and self.trex_pos == 2:
                    self.game_over = True
                    return
            
            # Increase score
            self.score += 1
            
            # Increase speed occasionally
            if self.score % 100 == 0 and self.game_speed > 0.05:
                self.game_speed *= 0.9
        
        def jump(self):
            if not self.is_jumping:
                self.is_jumping = True
                self.jump_height = self.max_jump
    
    print("🦖 T-Rex Run! 🦖")
    print("=" * 40)
    print("Jump over cacti to survive!")
    print("Press Space to jump, Q to quit")
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
    
    game = TRexGame()
    
    try:
        while not game.game_over:
            game.draw()
            
            # Non-blocking input check
            key = None
            for _ in range(10):  # Check multiple times per frame
                try:
                    key = get_key()
                    if key:
                        break
                except:
                    pass
                time.sleep(game.game_speed / 10)
            
            if key == ' ':
                game.jump()
            elif key == 'q' or key == 'Q':
                break
            
            game.update()
            time.sleep(game.game_speed)
        
        game.draw()
        
    except Exception as e:
        print(f"\nError: {e}")

# 46. 💣 Minesweeper

if __name__ == "__main__":
    trex_run()
