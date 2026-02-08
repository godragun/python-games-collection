import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def millionaire_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C",
            "value": 100
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B",
            "value": 500
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
            "answer": "B",
            "value": 1000
        }
    ]
    
    money = 0
    print("💰 Who Wants to Be a Millionaire 💰")
    print("=" * 40)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i} for ${q['value']}:")
        print(q['question'])
        for option in q['options']:
            print(option)
        
        while True:
            answer = input("\nYour answer (A/B/C/D) or 'quit': ").upper()
            if answer == 'QUIT':
                print(f"\nYou walked away with ${money}!")
                return
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid choice!")
        
        if answer == q['answer']:
            print(f"✅ Correct! You've won ${q['value']}")
            money = q['value']
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")
            print(f"\nGame Over! You won ${money}")
            break
    
    if money == questions[-1]['value']:
        print(f"\n🎊 Congratulations! You've won ${money}!")

# 6. ❓ Quiz Game

if __name__ == "__main__":
    millionaire_game()
