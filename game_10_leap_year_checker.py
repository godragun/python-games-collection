import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def leap_year_checker():
    print("🗓 Leap Year Checker 🗓")
    print("=" * 30)
    
    while True:
        try:
            year = int(input("\nEnter a year (or 0 to quit): "))
            if year == 0:
                break
            
            is_leap = False
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        is_leap = True
                else:
                    is_leap = True
            
            if is_leap:
                print(f"✅ {year} IS a leap year!")
            else:
                print(f"❌ {year} is NOT a leap year")
                
        except ValueError:
            print("Please enter a valid year")

# 11. ♣️ Baby Blackjack

if __name__ == "__main__":
    leap_year_checker()
