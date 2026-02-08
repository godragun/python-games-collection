import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def metrocard_calculator():
    print("🚇 NYC MetroCard Calculator 🚇")
    print("=" * 40)
    print("\nSingle ride: $2.90")
    print("Weekly pass: $34.00")
    print("Monthly pass: $132.00")
    
    while True:
        try:
            rides = int(input("\nHow many rides per month? "))
            days = int(input("How many days per week do you ride? "))
            
            single_cost = rides * 2.90
            weekly_cost = (days * 4.33) * 2.90  # Approximate weeks per month
            monthly_cost = 132.00
            
            print(f"\n💵 Cost Analysis:")
            print(f"Pay-per-ride: ${single_cost:.2f}")
            print(f"Weekly pass: ${weekly_cost:.2f}")
            print(f"Monthly pass: ${monthly_cost:.2f}")
            
            cheapest = min(single_cost, weekly_cost, monthly_cost)
            if cheapest == single_cost:
                print("\n💰 Cheapest: Pay-per-ride")
            elif cheapest == weekly_cost:
                print("\n💰 Cheapest: Weekly pass")
            else:
                print("\n💰 Cheapest: Monthly pass")
            
            again = input("\nCalculate again? (y/n): ").lower()
            if again != 'y':
                break
                
        except ValueError:
            print("Please enter valid numbers")

# 20. 🔐 Caesar Cipher

if __name__ == "__main__":
    metrocard_calculator()
