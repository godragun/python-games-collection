import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def area_calculator():
    import math
    
    print("📐 Area Calculator 📐")
    print("=" * 30)
    
    while True:
        print("\nChoose shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Trapezoid")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            side = float(input("Enter side length: "))
            area = side ** 2
            print(f"Area of square: {area:.2f}")
        elif choice == '2':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"Area of rectangle: {area:.2f}")
        elif choice == '3':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"Area of triangle: {area:.2f}")
        elif choice == '4':
            radius = float(input("Enter radius: "))
            area = math.pi * radius ** 2
            print(f"Area of circle: {area:.2f}")
        elif choice == '5':
            base1 = float(input("Enter first base: "))
            base2 = float(input("Enter second base: "))
            height = float(input("Enter height: "))
            area = 0.5 * (base1 + base2) * height
            print(f"Area of trapezoid: {area:.2f}")
        else:
            print("Invalid choice")

# 15. 🔢 Guess My Number

if __name__ == "__main__":
    area_calculator()
