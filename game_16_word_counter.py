import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def word_counter():
    print("🔡 Word Counter 🔡")
    print("=" * 30)
    
    while True:
        text = input("\nEnter text (or 'quit' to exit):\n")
        
        if text.lower() == 'quit':
            break
        
        words = text.split()
        characters = len(text)
        characters_no_spaces = len(text.replace(" ", ""))
        sentences = text.count('.') + text.count('!') + text.count('?')
        
        print("\n📊 Analysis:")
        print(f"Words: {len(words)}")
        print(f"Characters (total): {characters}")
        print(f"Characters (no spaces): {characters_no_spaces}")
        print(f"Sentences: {sentences}")
        
        if len(words) > 0:
            avg_word_length = sum(len(word) for word in words) / len(words)
            print(f"Average word length: {avg_word_length:.1f}")

# 17. 🆘 Morse Code Translator

if __name__ == "__main__":
    word_counter()
