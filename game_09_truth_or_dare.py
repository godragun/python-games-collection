import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def truth_or_dare():
    import random
    
    truths = [
        "What's your most embarrassing moment?",
        "Have you ever cheated on a test?",
        "What's your biggest fear?",
        "What's the silliest thing you've ever done?",
        "What's your secret talent?",
        "What's your most annoying habit?",
        "What's the biggest lie you've ever told?"
    ]
    
    dares = [
        "Do your best dance for 30 seconds",
        "Sing a song at the top of your lungs",
        "Talk in an accent for the next 3 minutes",
        "Do 10 pushups right now",
        "Text the 5th person in your contacts 'I love you'",
        "Let someone draw on your face with a pen",
        "Eat a spoonful of a condiment you don't like"
    ]
    
    print("🙈 Truth or Dare 🙈")
    print("=" * 30)
    
    while True:
        print("\nChoose: truth, dare, or quit")
        choice = input("> ").lower()
        
        if choice == 'quit':
            break
        elif choice == 'truth':
            print(f"\nTRUTH: {random.choice(truths)}")
        elif choice == 'dare':
            print(f"\nDARE: {random.choice(dares)}")
        else:
            print("Please choose 'truth' or 'dare'")

# 10. 🗓 Leap Year

if __name__ == "__main__":
    truth_or_dare()
