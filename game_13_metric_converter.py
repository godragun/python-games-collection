import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def metric_converter():
    print("📏 Metric Conversion Tool 📏")
    print("=" * 40)
    
    conversions = {
        '1': ('Length', {
            'cm to inches': lambda x: x / 2.54,
            'inches to cm': lambda x: x * 2.54,
            'meters to feet': lambda x: x * 3.28084,
            'feet to meters': lambda x: x / 3.28084,
            'km to miles': lambda x: x * 0.621371,
            'miles to km': lambda x: x / 0.621371
        }),
        '2': ('Temperature', {
            'Celsius to Fahrenheit': lambda x: (x * 9/5) + 32,
            'Fahrenheit to Celsius': lambda x: (x - 32) * 5/9,
            'Celsius to Kelvin': lambda x: x + 273.15,
            'Kelvin to Celsius': lambda x: x - 273.15
        }),
        '3': ('Weight', {
            'kg to pounds': lambda x: x * 2.20462,
            'pounds to kg': lambda x: x / 2.20462,
            'grams to ounces': lambda x: x * 0.035274,
            'ounces to grams': lambda x: x / 0.035274
        }),
        '4': ('Volume', {
            'liters to gallons': lambda x: x * 0.264172,
            'gallons to liters': lambda x: x / 0.264172,
            'ml to fluid ounces': lambda x: x * 0.033814,
            'fluid ounces to ml': lambda x: x / 0.033814
        })
    }
    
    while True:
        print("\nChoose conversion type:")
        for key, (name, _) in conversions.items():
            print(f"{key}. {name}")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        
        if choice in conversions:
            category, conv_dict = conversions[choice]
            print(f"\n{category} Conversions:")
            
            conv_list = list(conv_dict.items())
            for i, (name, _) in enumerate(conv_list, 1):
                print(f"{i}. {name}")
            
            try:
                conv_choice = int(input("\nSelect conversion: "))
                if 1 <= conv_choice <= len(conv_list):
                    conv_name, conv_func = conv_list[conv_choice-1]
                    value = float(input(f"Enter value to convert: "))
                    result = conv_func(value)
                    print(f"\n{value} {conv_name.split(' to ')[0]} = {result:.2f} {conv_name.split(' to ')[1]}")
                else:
                    print("Invalid choice")
            except ValueError:
                print("Please enter a number")
        else:
            print("Invalid choice")

# 14. 📐 Area Calculator

if __name__ == "__main__":
    metric_converter()
