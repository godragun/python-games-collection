import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def baby_blackjack():
    import random
    
    print("♣️ Baby Blackjack ♣️")
    print("=" * 30)
    print("\nRules: Get as close to 21 as possible without going over!")
    print("Aces count as 1, face cards as 10")
    
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    
    player_hand = [random.choice(deck), random.choice(deck)]
    dealer_hand = [random.choice(deck), random.choice(deck)]
    
    print(f"\nYour hand: {player_hand} = {sum(player_hand)}")
    print(f"Dealer shows: [{dealer_hand[0]}, ?]")
    
    # Player's turn
    while sum(player_hand) < 21:
        action = input("\nHit or Stand? ").lower()
        if action == 'hit':
            player_hand.append(random.choice(deck))
            print(f"Your hand: {player_hand} = {sum(player_hand)}")
        else:
            break
    
    player_total = sum(player_hand)
    
    if player_total > 21:
        print(f"\n💥 You bust with {player_total}! Dealer wins!")
        return
    
    # Dealer's turn
    print(f"\nDealer's hand: {dealer_hand} = {sum(dealer_hand)}")
    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(deck))
        print(f"Dealer hits: {dealer_hand} = {sum(dealer_hand)}")
    
    dealer_total = sum(dealer_hand)
    
    print(f"\nYour total: {player_total}")
    print(f"Dealer total: {dealer_total}")
    
    if dealer_total > 21:
        print("🎉 Dealer busts! You win!")
    elif player_total > dealer_total:
        print("🎉 You win!")
    elif player_total < dealer_total:
        print("💻 Dealer wins!")
    else:
        print("🤝 Push! It's a tie!")

# 12. ♣️ Blackjack

if __name__ == "__main__":
    baby_blackjack()
