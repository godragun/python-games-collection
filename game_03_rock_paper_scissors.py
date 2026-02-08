import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def rock_paper_scissors():
    import random
    
    choices = ["rock", "paper", "scissors"]
    wins = losses = ties = 0
    
    print("🪨 📄 ✂️ Rock Paper Scissors ✂️ 📄 🪨")
    print("=" * 40)
    
    while True:
        print(f"\nScore: You {wins} | Computer {losses} | Ties {ties}")
        print("\nChoose: rock, paper, scissors (or 'quit')")
        player = input("> ").lower()
        
        if player == 'quit':
            break
        if player not in choices:
            print("Invalid choice!")
            continue
        
        computer = random.choice(choices)
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("🤝 It's a tie!")
            ties += 1
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("🎉 You win!")
            wins += 1
        else:
            print("💻 Computer wins!")
            losses += 1

# 4. 🫱 Rock Paper Scissors Lizard Spock

if __name__ == "__main__":
    rock_paper_scissors()
