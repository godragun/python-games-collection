import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def roman_converter():
    roman_dict = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    def to_roman(num):
        result = ''
        for value, numeral in roman_dict.items():
            while num >= value:
                result += numeral
                num -= value
        return result
    
    def from_roman(roman):
        roman = roman.upper()
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        total = 0
        prev = 0
        
        for char in reversed(roman):
            value = values.get(char, 0)
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        return total
    
    print("🏛 Roman Numeral Converter 🏛")
    print("=" * 40)
    
    while True:
        print("\n1. Decimal to Roman")
        print("2. Roman to Decimal")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            try:
                num = int(input("Enter number (1-3999): "))
                if 1 <= num <= 3999:
                    print(f"Roman: {to_roman(num)}")
                else:
                    print("Number must be between 1 and 3999")
            except ValueError:
                print("Please enter a valid number")
        elif choice == '2':
            roman = input("Enter Roman numeral: ").upper()
            result = from_roman(roman)
            if result > 0:
                print(f"Decimal: {result}")
            else:
                print("Invalid Roman numeral")
        else:
            print("Invalid choice")

# 19. 🚇 NYC MetroCard Calculator

if __name__ == "__main__":
    roman_converter()
