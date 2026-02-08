import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def morse_translator():
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }
    
    reverse_morse = {value: key for key, value in morse_dict.items()}
    
    print("🔤 Morse Code Translator 🔤")
    print("=" * 40)
    
    while True:
        print("\n1. Text to Morse")
        print("2. Morse to Text")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            text = input("Enter text: ").upper()
            morse = []
            for char in text:
                if char in morse_dict:
                    morse.append(morse_dict[char])
                else:
                    morse.append('?')
            print(f"Morse: {' '.join(morse)}")
        elif choice == '2':
            morse = input("Enter Morse code (space between letters, / between words): ")
            text = []
            for code in morse.split(' '):
                if code == '/':
                    text.append(' ')
                elif code in reverse_morse:
                    text.append(reverse_morse[code])
                else:
                    text.append('?')
            print(f"Text: {''.join(text)}")
        else:
            print("Invalid choice")

# 18. 🏛 Roman Numeral Converter

if __name__ == "__main__":
    morse_translator()
