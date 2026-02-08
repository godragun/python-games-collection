import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def horoscope():
    import json
    import datetime
    
    horoscopes = {
        'aries': {
            'dates': 'Mar 21 - Apr 19',
            'traits': ['Courageous', 'Determined', 'Confident'],
            'today': 'Today is a good day to take initiative.'
        },
        'taurus': {
            'dates': 'Apr 20 - May 20',
            'traits': ['Reliable', 'Patient', 'Practical'],
            'today': 'Focus on stability and comfort today.'
        },
        'gemini': {
            'dates': 'May 21 - Jun 20',
            'traits': ['Gentle', 'Affectionate', 'Curious'],
            'today': 'Communication will be important today.'
        },
        'cancer': {
            'dates': 'Jun 21 - Jul 22',
            'traits': ['Tenacious', 'Highly imaginative', 'Loyal'],
            'today': 'Trust your intuition today.'
        },
        'leo': {
            'dates': 'Jul 23 - Aug 22',
            'traits': ['Creative', 'Passionate', 'Generous'],
            'today': 'Your charisma will shine today.'
        },
        'virgo': {
            'dates': 'Aug 23 - Sep 22',
            'traits': ['Loyal', 'Analytical', 'Kind'],
            'today': 'Pay attention to details today.'
        },
        'libra': {
            'dates': 'Sep 23 - Oct 22',
            'traits': ['Cooperative', 'Diplomatic', 'Gracious'],
            'today': 'Seek balance in all things today.'
        },
        'scorpio': {
            'dates': 'Oct 23 - Nov 21',
            'traits': ['Brave', 'Passionate', 'Stubborn'],
            'today': 'Depth and transformation are themes today.'
        },
        'sagittarius': {
            'dates': 'Nov 22 - Dec 21',
            'traits': ['Generous', 'Idealistic', 'Great sense of humor'],
            'today': 'Adventure awaits you today.'
        },
        'capricorn': {
            'dates': 'Dec 22 - Jan 19',
            'traits': ['Responsible', 'Disciplined', 'Self-control'],
            'today': 'Hard work will pay off today.'
        },
        'aquarius': {
            'dates': 'Jan 20 - Feb 18',
            'traits': ['Progressive', 'Original', 'Independent'],
            'today': 'Innovation is your friend today.'
        },
        'pisces': {
            'dates': 'Feb 19 - Mar 20',
            'traits': ['Compassionate', 'Artistic', 'Intuitive'],
            'today': 'Listen to your dreams today.'
        }
    }
    
    print("🪐 Daily Horoscope 🪐")
    print("=" * 40)
    
    while True:
        print("\nEnter your zodiac sign (or 'list' to see all, 'quit' to exit):")
        sign = input("> ").lower()
        
        if sign == 'quit':
            break
        elif sign == 'list':
            print("\nZodiac Signs:")
            for sign_name, data in horoscopes.items():
                print(f"{sign_name.capitalize():12} {data['dates']}")
        elif sign in horoscopes:
            data = horoscopes[sign]
            print(f"\n{sign.upper()}")
            print(f"Dates: {data['dates']}")
            print(f"Traits: {', '.join(data['traits'])}")
            print(f"\nToday's Horoscope:")
            print(data['today'])
            print(f"\nLucky Number: {datetime.datetime.now().day % 9 + 1}")
        else:
            print("Sign not found. Try 'list' to see all signs.")

# 23. 📋 To-Do Lists

if __name__ == "__main__":
    horoscope()
