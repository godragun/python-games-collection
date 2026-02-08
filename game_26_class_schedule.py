import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def class_schedule():
    import json
    
    filename = "schedule.json"
    
    def load_schedule():
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_schedule(schedule):
        with open(filename, 'w') as f:
            json.dump(schedule, f, indent=2)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    print("📝 Class Schedule Manager 📝")
    print("=" * 40)
    
    schedule = load_schedule()
    
    while True:
        print("\n1. Add Class")
        print("2. View Schedule")
        print("3. Remove Class")
        print("4. Today's Classes")
        print("5. Clear Schedule")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            day = input(f"Day ({', '.join(days)}): ").capitalize()
            if day in days:
                class_name = input("Class name: ")
                time = input("Time (e.g., 10:00 AM): ")
                location = input("Location: ")
                
                if day not in schedule:
                    schedule[day] = []
                
                schedule[day].append({
                    'name': class_name,
                    'time': time,
                    'location': location
                })
                schedule[day].sort(key=lambda x: x['time'])
                save_schedule(schedule)
                print("Class added!")
            else:
                print("Invalid day")
        elif choice == '2':
            if not schedule:
                print("Schedule is empty!")
            else:
                for day in days:
                    if day in schedule and schedule[day]:
                        print(f"\n{day}:")
                        for i, cls in enumerate(schedule[day], 1):
                            print(f"  {i}. {cls['time']} - {cls['name']} ({cls['location']})")
        elif choice == '3':
            day = input("Enter day: ").capitalize()
            if day in schedule and schedule[day]:
                print(f"\n{day}'s classes:")
                for i, cls in enumerate(schedule[day], 1):
                    print(f"{i}. {cls['time']} - {cls['name']}")
                try:
                    num = int(input("Enter class number to remove: "))
                    if 1 <= num <= len(schedule[day]):
                        removed = schedule[day].pop(num-1)
                        save_schedule(schedule)
                        print(f"Removed: {removed['name']}")
                    else:
                        print("Invalid number")
                except ValueError:
                    print("Please enter a number")
            else:
                print("No classes on that day")
        elif choice == '4':
            import datetime
            today = datetime.datetime.now().strftime('%A')
            print(f"\nToday is {today}")
            if today in schedule and schedule[today]:
                print("Today's classes:")
                for cls in schedule[today]:
                    print(f"- {cls['time']}: {cls['name']} ({cls['location']})")
            else:
                print("No classes today!")
        elif choice == '5':
            schedule = {}
            save_schedule(schedule)
            print("Schedule cleared!")
        else:
            print("Invalid choice")

# 27. 💸 Expense Tracker

if __name__ == "__main__":
    class_schedule()
