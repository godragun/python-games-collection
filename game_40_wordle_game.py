import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def wordle_game():
    import random
    import os
    
    # Word list (5-letter words)
    WORDS = [
        "apple", "brain", "chair", "dance", "earth", "flame", "grape", "house",
        "image", "joker", "knife", "lemon", "music", "night", "ocean", "piano",
        "queen", "river", "snake", "table", "umbra", "voice", "water", "yacht",
        "zebra", "cloud", "dream", "fruit", "ghost", "happy", "irony", "jelly"
    ]
    
    class Wordle:
        def __init__(self):
            self.secret_word = random.choice(WORDS)
            self.guesses = []
            self.max_attempts = 6
            self.game_over = False
        
        def draw(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("🟩 WORDLE 🟩")
            print("=" * 30)
            print(f"Attempts: {len(self.guesses)}/{self.max_attempts}")
            print()
            
            # Draw previous guesses
            for guess in self.guesses:
                display = ""
                for i, letter in enumerate(guess):
                    if letter == self.secret_word[i]:
                        display += "🟩"  # Correct letter and position
                    elif letter in self.secret_word:
                        display += "🟨"  # Correct letter, wrong position
                    else:
                        display += "⬜"  # Wrong letter
                print(display)
            
            # Draw empty lines for remaining attempts
            for _ in range(self.max_attempts - len(self.guesses)):
                print("⬜⬜⬜⬜⬜")
            
            print()
            
            if self.game_over:
                if self.guesses and self.guesses[-1] == self.secret_word:
                    print("🎉 Congratulations! You guessed the word!")
                else:
                    print(f"💀 Game Over! The word was: {self.secret_word}")
            else:
                print("Enter a 5-letter word (or 'quit' to exit)")
        
        def make_guess(self, guess):
            guess = guess.lower().strip()
            
            if guess == 'quit':
                self.game_over = True
                return
            
            if len(guess) != 5:
                print("Word must be 5 letters!")
                input("Press Enter to continue...")
                return False
            
            if guess not in WORDS:
                print("Not in word list!")
                input("Press Enter to continue...")
                return False
            
            self.guesses.append(guess)
            
            if guess == self.secret_word:
                self.game_over = True
                return True
            
            if len(self.guesses) >= self.max_attempts:
                self.game_over = True
            
            return True
    
    print("🟩 Wordle Game 🟩")
    print("=" * 40)
    print("Guess the 5-letter word in 6 attempts!")
    print("🟩 = Correct letter and position")
    print("🟨 = Correct letter, wrong position")
    print("⬜ = Letter not in word")
    input("\nPress Enter to start...")
    
    game = Wordle()
    
    while not game.game_over:
        game.draw()
        
        guess = input("\nYour guess: ")
        
        if guess.lower() == 'quit':
            break
        
        game.make_guess(guess)
    
    game.draw()

# 41. ⏰ GUI Alarm Clock (simplified terminal version)


if __name__ == "__main__":
    wordle_game()
