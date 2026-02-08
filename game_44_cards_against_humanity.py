import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def cards_against_humanity():
    import random
    
    black_cards = [
        "Why can't I sleep at night?",
        "What's that smell?",
        "I got 99 problems but _ ain't one.",
        "What's the next Happy Meal toy?",
        "What will always get you laid?",
        "What did I bring back from Mexico?",
        "What's there a ton of in heaven?",
        "What would grandma find disturbing, yet oddly charming?",
        "What did the US airdrop to the children of Afghanistan?",
        "What helps Obama unwind?"
    ]
    
    white_cards = [
        "A micropenis.",
        "A pangender octopus who roams the cosmos in search of love.",
        "The arrival of the pizza.",
        "An oversized lollipop.",
        "Being a motherfucking sorcerer.",
        "Bees?",
        "Getting drunk on mouthwash.",
        "These hoes.",
        "Giving 110%.",
        "Hot cheese.",
        "A middle-aged man on roller skates.",
        "Coat hanger abortions.",
        "GoGurt.",
        "Holding up a gas station.",
        "The Pope.",
        "A mime having a stroke.",
        "Stephen Hawking talking dirty.",
        "Object permanence.",
        "Daddy issues.",
        "Racism.",
        "Passive-aggressive Post-it notes.",
        "A Super Soaker full of cat pee.",
        "Pretending to care.",
        "Public ridicule.",
        "A lifetime of sadness.",
        "An AK-47 assault rifle.",
        "Cards Against Humanity."
    ]
    
    print("◼️ Cards Against Humanity (Simplified) ◼️")
    print("=" * 50)
    
    random.shuffle(black_cards)
    random.shuffle(white_cards)
    
    score = {"Player": 0, "Computer": 0}
    round_num = 1
    
    while white_cards and black_cards and round_num <= 5:
        print(f"\n--- Round {round_num} ---")
        print(f"Score: Player {score['Player']} - Computer {score['Computer']}")
        
        # Draw black card
        black_card = black_cards.pop()
        print(f"\nBlack Card: {black_card}")
        
        # Player chooses white cards
        print(f"\nYour white cards:")
        player_cards = [white_cards.pop() for _ in range(5)]
        for i, card in enumerate(player_cards, 1):
            print(f"{i}. {card}")
        
        try:
            choice = int(input("\nChoose a card (1-5): ")) - 1
            if 0 <= choice < 5:
                player_choice = player_cards[choice]
                print(f"\nYou played: {player_choice}")
            else:
                print("Invalid choice, using first card")
                player_choice = player_cards[0]
        except:
            print("Invalid choice, using first card")
            player_choice = player_cards[0]
        
        # Computer chooses
        computer_cards = [white_cards.pop() for _ in range(5)]
        computer_choice = random.choice(computer_cards)
        print(f"Computer played: {computer_choice}")
        
        # Judge (random)
        judge = random.choice(["Player", "Computer"])
        print(f"\n{judge} is the judge!")
        
        if judge == "Player":
            print("Which card is funnier?")
            print(f"1. {player_choice}")
            print(f"2. {computer_choice}")
            try:
                winner = int(input("Choose 1 or 2: "))
                if winner == 1:
                    score["Player"] += 1
                    print("You win the round!")
                else:
                    score["Computer"] += 1
                    print("Computer wins the round!")
            except:
                # Random if player doesn't choose
                if random.random() > 0.5:
                    score["Player"] += 1
                    print("You win the round!")
                else:
                    score["Computer"] += 1
                    print("Computer wins the round!")
        else:
            # Computer judges randomly
            if random.random() > 0.5:
                score["Computer"] += 1
                print("Computer chooses its own card! Computer wins!")
            else:
                score["Player"] += 1
                print("Computer chooses your card! You win!")
        
        round_num += 1
        input("\nPress Enter to continue...")
    
    print(f"\n=== FINAL SCORE ===")
    print(f"Player: {score['Player']}")
    print(f"Computer: {score['Computer']}")
    
    if score['Player'] > score['Computer']:
        print("🎉 You win!")
    elif score['Player'] < score['Computer']:
        print("💻 Computer wins!")
    else:
        print("🤝 It's a tie!")

# 45. 🦖 T-Rex Run! (terminal version)


if __name__ == "__main__":
    cards_against_humanity()
