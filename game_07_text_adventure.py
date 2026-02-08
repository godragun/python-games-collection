import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def text_adventure():
    print("⚔️ Text Adventure: The Lost Temple ⚔️")
    print("=" * 40)
    print("\nYou find yourself at the entrance of an ancient temple.")
    print("Two paths lie before you: left and right.")
    
    # First decision
    choice1 = input("\nDo you go left or right? ").lower()
    
    if 'left' in choice1:
        print("\nYou enter a room filled with treasure!")
        print("But there's a sleeping dragon guarding it.")
        choice2 = input("\nDo you (1) Try to sneak past or (2) Leave quietly? ")
        
        if choice2 == '1':
            print("\nThe dragon wakes up! Game Over! 🐉")
        else:
            print("\nYou leave safely with a small gem. You win! 💎")
    
    elif 'right' in choice1:
        print("\nYou enter a dark corridor.")
        print("You see a faint light ahead and hear water dripping.")
        choice2 = input("\nDo you (1) Go toward the light or (2) Investigate the sound? ")
        
        if choice2 == '1':
            print("\nYou find the temple's exit! You win! 🏆")
        else:
            print("\nYou fall into a pit! Game Over! 🕳️")
    else:
        print("\nYou hesitate too long and the entrance collapses. Game Over!")

# 8. 🤖 Chatbot

if __name__ == "__main__":
    text_adventure()
