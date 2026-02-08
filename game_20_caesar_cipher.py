import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def caesar_cipher():
    print("🔐 Caesar Cipher 🔐")
    print("=" * 30)
    
    def encrypt(text, shift):
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        return result
    
    def decrypt(text, shift):
        return encrypt(text, -shift)
    
    def brute_force(text):
        print("\n🔍 Brute Force Decryption:")
        for shift in range(26):
            print(f"Shift {shift:2}: {decrypt(text, shift)}")
    
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        
        if choice in ['1', '2']:
            text = input("Enter text: ")
            try:
                shift = int(input("Enter shift (0-25): "))
                if not (0 <= shift <= 25):
                    print("Shift must be 0-25")
                    continue
                
                if choice == '1':
                    print(f"Encrypted: {encrypt(text, shift)}")
                else:
                    print(f"Decrypted: {decrypt(text, shift)}")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '3':
            text = input("Enter encrypted text: ")
            brute_force(text)
        
        else:
            print("Invalid choice")

# ==================== LEVEL 2 PROJECTS ====================

# 21. 🏦 Bank Account

if __name__ == "__main__":
    caesar_cipher()
