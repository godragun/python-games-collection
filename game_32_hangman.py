import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def hangman():
    import random
    
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 
             'function', 'variable', 'constant', 'iterator', 'dictionary']
    
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    wrong_letters = []
    
    hangman_parts = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    
    print("🪦 Hangman 🪦")
    print("=" * 40)
    
    while attempts > 0 and '_' in guessed:
        print(hangman_parts[6 - attempts])
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Wrong letters: {', '.join(wrong_letters)}")
        print(f"Attempts left: {attempts}")
        
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue
        
        if guess in wrong_letters or guess in guessed:
            print("You already guessed that letter")
            continue
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            wrong_letters.append(guess)
            attempts -= 1
            print("Wrong guess!")
    
    print(hangman_parts[6 - attempts])
    
    if '_' not in guessed:
        print(f"\n🎉 Congratulations! You guessed: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")

# 33. ❌ Tic-Tac-Toe

if __name__ == "__main__":
    hangman()
