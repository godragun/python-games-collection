import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def blackjack():
    import random
    
    class Card:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value
        
        def __repr__(self):
            return f"{self.value}{self.suit}"
    
    class Deck:
        def __init__(self):
            suits = ['♠', '♥', '♦', '♣']
            values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            self.cards = [Card(suit, value) for suit in suits for value in values]
            random.shuffle(self.cards)
        
        def deal(self):
            return self.cards.pop()
    
    def hand_value(hand):
        value = 0
        aces = 0
        
        for card in hand:
            if card.value in ['J','Q','K']:
                value += 10
            elif card.value == 'A':
                value += 11
                aces += 1
            else:
                value += int(card.value)
        
        while value > 21 and aces:
            value -= 10
            aces -= 1
        
        return value
    
    print("♣️ ♠️ ♥️ ♦️ Blackjack ♦️ ♥️ ♠️ ♣️")
    print("=" * 40)
    
    deck = Deck()
    player_hand = [deck.deal(), deck.deal()]
    dealer_hand = [deck.deal(), deck.deal()]
    
    print(f"\nYour hand: {player_hand} = {hand_value(player_hand)}")
    print(f"Dealer shows: [{dealer_hand[0]}, ?]")
    
    # Player's turn
    while hand_value(player_hand) < 21:
        action = input("\nHit, Stand, or Double? ").lower()
        if action == 'hit':
            player_hand.append(deck.deal())
            print(f"Your hand: {player_hand} = {hand_value(player_hand)}")
        elif action == 'double':
            player_hand.append(deck.deal())
            print(f"Your hand: {player_hand} = {hand_value(player_hand)}")
            break
        else:
            break
    
    player_total = hand_value(player_hand)
    
    if player_total > 21:
        print(f"\n💥 Bust! You have {player_total}")
        return
    
    # Dealer's turn
    print(f"\nDealer's hand: {dealer_hand} = {hand_value(dealer_hand)}")
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.deal())
        print(f"Dealer hits: {dealer_hand} = {hand_value(dealer_hand)}")
    
    dealer_total = hand_value(dealer_hand)
    
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

# 13. 📏 Metric Conversion Tool

if __name__ == "__main__":
    blackjack()
