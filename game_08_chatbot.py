import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! What's up?",
        "how are you": "I'm just a program, but I'm functioning well!",
        "what's your name": "I'm Python Bot, nice to meet you!",
        "bye": "Goodbye! Have a great day!",
        "weather": "I can't check the weather, but I hope it's nice!",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "help": "I can chat about simple things. Try saying hello or ask for a joke!",
        "time": f"The current time is {time.strftime('%H:%M')}",
        "date": f"Today is {time.strftime('%Y-%m-%d')}"
    }
    
    print("🤖 Python Chatbot 🤖")
    print("=" * 30)
    print("Type 'bye' to exit")
    print("Try: hello, how are you, joke, weather, time, date, help")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if user_input == 'bye':
            print("Bot: Goodbye! 👋")
            break
        
        response = "I'm not sure how to respond to that."
        for key in responses:
            if key in user_input:
                response = responses[key]
                break
        
        print(f"Bot: {response}")

# 9. 🙈 Truth or Dare

if __name__ == "__main__":
    chatbot()
