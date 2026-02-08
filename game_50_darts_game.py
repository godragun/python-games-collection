import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def darts_game():
    import random
    
    class Darts:
        def __init__(self):
            self.player_score = 501
            self.computer_score = 501
            self.round = 1
            self.winning_score = 0
        
        def throw_dart(self, player_type="player"):
            # Simulate a dart throw
            scores = []
            total = 0
            
            for _ in range(3):  # 3 darts per turn
                # Random score with probabilities
                rand = random.random()
                if rand < 0.05:  # 5% chance bullseye
                    score = 50
                    area = "BULLSEYE! 🎯"
                elif rand < 0.15:  # 10% chance outer bull
                    score = 25
                    area = "Outer Bull"
                elif rand < 0.4:  # 25% chance triple
                    number = random.randint(1, 20)
                    score = number * 3
                    area = f"Triple {number}"
                elif rand < 0.7:  # 30% chance double
                    number = random.randint(1, 20)
                    score = number * 2
                    area = f"Double {number}"
                else:  # 30% chance single
                    number = random.randint(1, 20)
                    score = number
                    area = f"Single {number}"
                
                scores.append((score, area))
                total += score
            
            return scores, total
        
        def player_turn(self):
            print(f"\n🎯 Your turn (Score: {self.player_score})")
            input("Press Enter to throw...")
            
            scores, total = self.throw_dart("player")
            
            print("Your throws:")
            for i, (score, area) in enumerate(scores, 1):
                print(f"  Dart {i}: {area} ({score} points)")
            
            print(f"  Total this turn: {total}")
            
            # Check if score would go below 0 or end exactly at 1
            new_score = self.player_score - total
            if new_score < 0 or new_score == 1:
                print("  No score - bust!")
                return False
            elif new_score == 0:
                print("  🎉 CHECKOUT! You win!")
                self.player_score = 0
                return True
            else:
                self.player_score = new_score
                return False
        
        def computer_turn(self):
            print(f"\n💻 Computer's turn (Score: {self.computer_score})")
            
            scores, total = self.throw_dart("computer")
            
            print("Computer throws:")
            for i, (score, area) in enumerate(scores, 1):
                print(f"  Dart {i}: {area} ({score} points)")
            
            print(f"  Total this turn: {total}")
            
            # Computer logic: avoid busting
            new_score = self.computer_score - total
            if new_score < 0 or new_score == 1:
                print("  Computer busts!")
                return False
            elif new_score == 0:
                print("  💻 Computer wins!")
                self.computer_score = 0
                return True
            else:
                self.computer_score = new_score                return False
        
        def play(self):
            print("🎯 501 Darts 🎯")
            print("=" * 40)
            print("Start from 501, reach exactly 0")
            print("Last dart must be a double or bullseye")
            print("If you go below 0 or reach 1, you bust!")
            
            while self.player_score > 0 and self.computer_score > 0:
                print(f"\n=== ROUND {self.round} ===")
                
                # Player turn
                if self.player_turn():
                    break
                
                # Computer turn
                if self.computer_turn():
                    break
                
                self.round += 1
            
            print(f"\n{'='*40}")
            if self.player_score == 0:
                print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
            else:
                print("💻 Computer wins!")
            print(f"Final score: You {self.player_score} - Computer {self.computer_score}")
    
    game = Darts()
    game.play()

# Update main menu to include all 50 projects

if __name__ == "__main__":
    darts_game()
