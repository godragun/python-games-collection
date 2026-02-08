import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def guess_number():
    import random
    
    print("🔢 Guess My Number 🔢")
    print("=" * 30)
    
    while True:
        print("\nChoose difficulty:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-500)")
        print("0. Exit")
        
        choice = input("> ")
        
        if choice == '0':
            break
        
        if choice == '1':
            max_num = 50
            max_attempts = 10
        elif choice == '2':
            max_num = 100
            max_attempts = 7
        elif choice == '3':
            max_num = 500
            max_attempts = 5
        else:
            print("Invalid choice")
            continue
        
        number = random.randint(1, max_num)
        attempts = 0
        
        print(f"\nI'm thinking of a number between 1 and {max_num}")
        print(f"You have {max_attempts} attempts")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: "))
                attempts += 1
                
                if guess < number:
                    print("📈 Too low!")
                elif guess > number:
                    print("📉 Too high!")
                else:
                    print(f"🎉 Correct! You guessed it in {attempts} attempts!")
                    break
                
                if attempts == max_attempts:
                    print(f"\n💔 Game Over! The number was {number}")
            except ValueError:
                print("Please enter a valid number")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break

# 16. 🔡 Word Counter

if __name__ == "__main__":
    guess_number()
