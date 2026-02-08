import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def rock_paper_scissors_lizard_spock():
    import random
    
    choices = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }
    
    print("🪨 📄 ✂️ 🦎 🖖 Rock Paper Scissors Lizard Spock 🖖 🦎 ✂️ 📄 🪨")
    print("=" * 60)
    print("\nRules:")
    print("- Scissors cuts Paper")
    print("- Paper covers Rock")
    print("- Rock crushes Lizard")
    print("- Lizard poisons Spock")
    print("- Spock smashes Scissors")
    print("- Scissors decapitates Lizard")
    print("- Lizard eats Paper")
    print("- Paper disproves Spock")
    print("- Spock vaporizes Rock")
    print("- Rock crushes Scissors")
    
    wins = losses = ties = 0
    
    while True:
        print(f"\nScore: You {wins} | Computer {losses} | Ties {ties}")
        print("\nChoose: rock, paper, scissors, lizard, spock (or 'quit')")
        player = input("> ").lower()
        
        if player == 'quit':
            break
        if player not in choices:
            print("Invalid choice!")
            continue
        
        computer = random.choice(list(choices.keys()))
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("🤝 It's a tie!")
            ties += 1
        elif computer in choices[player]:
            print(f"🎉 {player.capitalize()} beats {computer}! You win!")
            wins += 1
        else:
            print(f"💻 {computer.capitalize()} beats {player}! Computer wins!")
            losses += 1

# 5. 🤑 Who Wants to Be a Millionaire

if __name__ == "__main__":
    rock_paper_scissors_lizard_spock()
