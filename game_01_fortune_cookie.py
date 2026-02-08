import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
import random
import time

def fortune_cookie():
    fortunes = [
        "You will have a great day today!",
        "Good news will come to you by mail.",
        "You will become great if you believe in yourself.",
        "Now is the time to try something new.",
        "Your hard work will soon pay off.",
        "A pleasant surprise is waiting for you.",
        "You will travel to many exotic places in your lifetime.",
        "Your ability to juggle many tasks will take you far.",
        "A dream you have will come true.",
        "You will receive money from an unexpected source."
    ]
    
    print("🥠 Fortune Cookie Simulator 🥠")
    print("=" * 30)
    print("Opening your fortune cookie...")
    time.sleep(1.5)
    print(f"\nYour fortune: {random.choice(fortunes)}")
    print("\nLucky numbers:", ' '.join(str(random.randint(1, 99)) for _ in range(6)))

# 2. 🎲 Dice Rolling Simulator

if __name__ == "__main__":
    fortune_cookie()
