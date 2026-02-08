import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def space_invaders():
    import random
    import time
    import os
    
    class SpaceInvaders:
        def __init__(self, width=40, height=20):
            self.width = width
            self.height = height
            self.reset()
        
        def reset(self):
            self.player_x = self.width // 2
            self.invaders = []
            self.bullets = []
            self.invader_direction = 1
            self.score = 0
            self.lives = 3
            self.game_over = False
            
            # Create invaders
            for row in range(3):
                for col in range(8):
                    self.invaders.append([col * 4 + 2, row * 2 + 2])
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("👾 SPACE INVADERS 👾")
            print(f"Score: {self.score}  Lives: {'♥' * self.lives}")
            print("=" * (self.width + 2))
            
            for y in range(self.height):
                line = "|"
                for x in range(self.width):
                    # Draw player
                    if y == self.height - 1 and abs(x - self.player_x) <= 1:
                        line += "▲"
                    # Draw invaders
                    elif [x, y] in self.invaders:
                        line += "👾"
                    # Draw bullets
                    elif [x, y] in self.bullets:
                        line += "•"
                    else:
                        line += " "
                line += "|"
                print(line)
            
            print("=" * (self.width + 2))
            print("Controls: A/D to move, Space to shoot, Q to quit")
            
            if self.game_over:
                print("\n💀 GAME OVER!")
                print(f"Final Score: {self.score}")
        
        def update(self, move_left=False, move_right=False, shoot=False):
            if self.game_over:
                return
            
            # Move player
            if move_left and self.player_x > 1:
                self.player_x -= 1
            if move_right and self.player_x < self.width - 2:
                self.player_x += 1
            
            # Shoot bullet
            if shoot:
                self.bullets.append([self.player_x, self.height - 2])
            
            # Move bullets
            new_bullets = []
            for bullet in self.bullets:
                bullet[1] -= 1
                if bullet[1] > 0:
                    new_bullets.append(bullet)
            self.bullets = new_bullets
            
            # Move invaders
            move_down = False
            for invader in self.invaders:
                invader[0] += self.invader_direction
                if invader[0] <= 0 or invader[0] >= self.width - 1:
                    move_down = True
            
            if move_down:
                self.invader_direction *= -1
                for invader in self.invaders:
                    invader[1] += 1
                    if invader[1] >= self.height - 1:
                        self.lives -= 1
            
            # Check bullet collisions
            bullets_to_remove = []
            invaders_to_remove = []
            
            for bullet in self.bullets:
                for invader in self.invaders:
                    if bullet[0] == invader[0] and bullet[1] == invader[1]:
                        bullets_to_remove.append(bullet)
                        invaders_to_remove.append(invader)
                        self.score += 100
            
            self.bullets = [b for b in self.bullets if b not in bullets_to_remove]
            self.invaders = [i for i in self.invaders if i not in invaders_to_remove]
            
            # Check if invaders reached bottom
            for invader in self.invaders:
                if invader[1] >= self.height - 1:
                    self.lives -= 1
                    self.invaders.remove(invader)
            
            # Check game over
            if not self.invaders:
                print("\n🎉 YOU WIN!")
                self.game_over = True
            elif self.lives <= 0:
                self.game_over = True
    
    print("👾 Space Invaders 👾")
    print("=" * 40)
    print("Destroy all aliens before they reach Earth!")
    print("Controls: A/D = Move, Space = Shoot")
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
    
    game = SpaceInvaders()
    
    try:
        while not game.game_over:
            game.draw()
            
            key = get_key()
            move_left = key == 'a' or key == 'A'
            move_right = key == 'd' or key == 'D'
            shoot = key == ' '
            
            if key == 'q' or key == 'Q':
                break
            
            game.update(move_left, move_right, shoot)
            time.sleep(0.1)
        
        game.draw()
    
    except Exception as e:
        print(f"\nError: {e}")

# 39. 🧠 2048 Game

if __name__ == "__main__":
    space_invaders()
