import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def quiz_game():
    import json
    import random
    
    questions = [
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the color of the sky?",
            "options": ["Red", "Green", "Blue", "Yellow"],
            "answer": "Blue"
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        }
    ]
    
    print("❓ Quiz Game ❓")
    print("=" * 30)
    score = 0
    
    random.shuffle(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        
        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("Please enter 1-4")
            except ValueError:
                print("Please enter a number")
        
        if q['options'][answer-1] == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The answer is {q['answer']}")
    
    print(f"\n🎯 Final Score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

# 7. ⚔️ Text-Based Adventure

if __name__ == "__main__":
    quiz_game()
