import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import time

def dice_roller():
    import random
    
    print("🎲 Dice Rolling Simulator 🎲")
    print("=" * 30)
    
    while True:
        try:
            num_dice = int(input("How many dice to roll? (1-5): "))
            if 1 <= num_dice <= 5:
                break
            else:
                print("Please enter 1-5")
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            sides = int(input("How many sides per die? (4, 6, 8, 10, 12, 20): "))
            if sides in [4, 6, 8, 10, 12, 20]:
                break
            else:
                print("Invalid number of sides")
        except ValueError:
            print("Please enter a valid number")
    
    results = [random.randint(1, sides) for _ in range(num_dice)]
    
    print(f"\n🎲 Rolling {num_dice}d{sides}...")
    time.sleep(1)
    print(f"\nResults: {results}")
    print(f"Total: {sum(results)}")
    
    # Special messages
    if sides == 20 and num_dice == 1:
        if results[0] == 20:
            print("🎯 NATURAL 20! Critical hit!")
        elif results[0] == 1:
            print("💀 Critical fail!")

# 3. 🫱 Rock Paper Scissors

if __name__ == "__main__":
    dice_roller()
