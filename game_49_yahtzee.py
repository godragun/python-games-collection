import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def yahtzee_game():
    import random
    
    class Yahtzee:
        def __init__(self):
            self.dice = [0] * 5
            self.rolls_left = 3
            self.scores = {
                'Ones': None, 'Twos': None, 'Threes': None,
                'Fours': None, 'Fives': None, 'Sixes': None,
                'Three of a Kind': None, 'Four of a Kind': None,
                'Full House': None, 'Small Straight': None,
                'Large Straight': None, 'Yahtzee': None, 'Chance': None
            }
            self.upper_bonus = 0
            self.total_score = 0
        
        def roll_dice(self, keep=None):
            if keep is None:
                keep = []
            
            self.rolls_left -= 1
            for i in range(5):
                if i not in keep:
                    self.dice[i] = random.randint(1, 6)
        
        def calculate_score(self, category):
            if category in ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']:
                number = int(category[0]) if category[0].isdigit() else 1
                return sum(die for die in self.dice if die == number)
            
            elif category == 'Three of a Kind':
                for value in range(1, 7):
                    if self.dice.count(value) >= 3:
                        return sum(self.dice)
                return 0
            
            elif category == 'Four of a Kind':
                for value in range(1, 7):
                    if self.dice.count(value) >= 4:
                        return sum(self.dice)
                return 0
            
            elif category == 'Full House':
                counts = [self.dice.count(value) for value in range(1, 7)]
                if 3 in counts and 2 in counts:
                    return 25
                return 0
            
            elif category == 'Small Straight':
                sorted_dice = sorted(set(self.dice))
                if len(sorted_dice) >= 4:
                    for i in range(len(sorted_dice) - 3):
                        if sorted_dice[i:i+4] == list(range(sorted_dice[i], sorted_dice[i]+4)):
                            return 30
                return 0
            
            elif category == 'Large Straight':
                if sorted(self.dice) in [[1,2,3,4,5], [2,3,4,5,6]]:
                    return 40
                return 0
            
            elif category == 'Yahtzee':
                if len(set(self.dice)) == 1:
                    return 50
                return 0
            
            elif category == 'Chance':
                return sum(self.dice)
            
            return 0
        
        def show_dice(self):
            print("\nYour dice: ", end="")
            for i, die in enumerate(self.dice):
                print(f"{i+1}:{die} ", end="")
            print(f"(Rolls left: {self.rolls_left})")
        
        def show_scorecard(self):
            print("\nSCORECARD:")
            print("-" * 40)
            
            # Upper section
            upper_total = 0
            for cat in ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']:
                score = self.scores[cat]
                if score is not None:
                    upper_total += score
                    print(f"{cat:20} {score:3}")
                else:
                    possible = self.calculate_score(cat)
                    print(f"{cat:20} -   (possible: {possible})")
            
            if upper_total >= 63:
                self.upper_bonus = 35
            print(f"Upper Bonus: {self.upper_bonus}")
            print(f"Upper Total: {upper_total + self.upper_bonus}")
            
            print("-" * 40)
            
            # Lower section
            lower_total = 0
            for cat in ['Three of a Kind', 'Four of a Kind', 'Full House',
                       'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']:
                score = self.scores[cat]
                if score is not None:
                    lower_total += score
                    print(f"{cat:20} {score:3}")
                else:
                    possible = self.calculate_score(cat)
                    print(f"{cat:20} -   (possible: {possible})")
            
            print(f"Lower Total: {lower_total}")
            print("-" * 40)
            print(f"GRAND TOTAL: {upper_total + self.upper_bonus + lower_total}")
        
        def play_turn(self):
            self.rolls_left = 3
            self.dice = [0] * 5
            
            # First roll
            print("\nFirst roll:")
            self.roll_dice()
            self.show_dice()
            
            # Second and third rolls
            while self.rolls_left > 0:
                choice = input("\nEnter dice to keep (1-5, space separated) or 'roll': ")
                
                if choice.lower() == 'roll':
                    break
                
                try:
                    keep = [int(x)-1 for x in choice.split() if 1 <= int(x) <= 5]
                    self.roll_dice(keep)
                    self.show_dice()
                except ValueError:
                    print("Invalid input")
            
            # Choose category
            print("\nAvailable categories:")
            available = [cat for cat, score in self.scores.items() if score is None]
            for i, cat in enumerate(available, 1):
                possible = self.calculate_score(cat)
                print(f"{i}. {cat:20} (score: {possible})")
            
            while True:
                try:
                    choice = int(input("\nChoose category number: "))
                    if 1 <= choice <= len(available):
                        category = available[choice-1]
                        score = self.calculate_score(category)
                        self.scores[category] = score
                        print(f"Scored {score} points for {category}")
                        break
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a number")
    
    print("🎲 Yahtzee 🎲")
    print("=" * 40)
    print("Roll 5 dice and score points in 13 categories")
    
    game = Yahtzee()
    
    for turn in range(1, 14):
        print(f"\n=== TURN {turn}/13 ===")
        game.show_scorecard()
        game.play_turn()
    
    print("\n=== FINAL SCORE ===")
    game.show_scorecard()

# 50. 🎯 Darts (scoring game)


if __name__ == "__main__":
    yahtzee_game()
