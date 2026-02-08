import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def alarm_clock():
    import datetime
    import time
    import winsound  # Windows only, for other OS need different sound library
    import threading
    import os
    
    class AlarmClock:
        def __init__(self):
            self.alarms = []
            self.load_alarms()
        
        def load_alarms(self):
            try:
                with open("alarms.txt", "r") as f:
                    for line in f:
                        if line.strip():
                            time_str, label = line.strip().split("|")
                            hour, minute = map(int, time_str.split(":"))
                            self.alarms.append({
                                "time": datetime.time(hour, minute),
                                "label": label,
                                "enabled": True
                            })
            except FileNotFoundError:
                pass
        
        def save_alarms(self):
            with open("alarms.txt", "w") as f:
                for alarm in self.alarms:
                    time_str = alarm["time"].strftime("%H:%M")
                    f.write(f"{time_str}|{alarm['label']}\n")
        
        def add_alarm(self, hour, minute, label=""):
            alarm_time = datetime.time(hour, minute)
            self.alarms.append({
                "time": alarm_time,
                "label": label,
                "enabled": True
            })
            self.save_alarms()
            print(f"Alarm set for {hour:02d}:{minute:02d}")
        
        def check_alarms(self):
            current_time = datetime.datetime.now().time()
            for alarm in self.alarms:
                if (alarm["enabled"] and 
                    alarm["time"].hour == current_time.hour and
                    alarm["time"].minute == current_time.minute):
                    return alarm
            return None
        
        def list_alarms(self):
            if not self.alarms:
                print("No alarms set")
                return
            
            print("\n⏰ Current Alarms:")
            for i, alarm in enumerate(self.alarms, 1):
                status = "✓" if alarm["enabled"] else "✗"
                label = alarm["label"] if alarm["label"] else "(no label)"
                print(f"{i}. [{status}] {alarm['time'].strftime('%H:%M')} - {label}")
        
        def delete_alarm(self, index):
            if 1 <= index <= len(self.alarms):
                removed = self.alarms.pop(index - 1)
                self.save_alarms()
                print(f"Deleted alarm: {removed['time'].strftime('%H:%M')}")
            else:
                print("Invalid alarm number")
        
        def toggle_alarm(self, index):
            if 1 <= index <= len(self.alarms):
                self.alarms[index - 1]["enabled"] = not self.alarms[index - 1]["enabled"]
                self.save_alarms()
                status = "enabled" if self.alarms[index - 1]["enabled"] else "disabled"
                print(f"Alarm {status}")
            else:
                print("Invalid alarm number")
    
    def alarm_monitor(clock):
        while True:
            alarm = clock.check_alarms()
            if alarm:
                print(f"\n🔔 ALARM! {alarm['time'].strftime('%H:%M')} - {alarm['label']}")
                
                # Sound alarm (Windows only)
                try:
                    for _ in range(10):
                        winsound.Beep(1000, 500)
                        time.sleep(0.5)
                except:
                    print("BEEP! BEEP! BEEP!")
                
                # Disable the alarm after it goes off
                for a in clock.alarms:
                    if a["time"] == alarm["time"]:
                        a["enabled"] = False
                clock.save_alarms()
            
            time.sleep(30)  # Check every 30 seconds
    
    print("⏰ Alarm Clock ⏰")
    print("=" * 40)
    
    clock = AlarmClock()
    
    # Start alarm monitoring in background thread
    monitor_thread = threading.Thread(target=alarm_monitor, args=(clock,), daemon=True)
    monitor_thread.start()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\nCurrent time: {current_time}")
        
        print("\n1. Set new alarm")
        print("2. List alarms")
        print("3. Delete alarm")
        print("4. Toggle alarm")
        print("5. View upcoming alarms")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            try:
                hour = int(input("Hour (0-23): "))
                minute = int(input("Minute (0-59): "))
                label = input("Label (optional): ")
                
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    clock.add_alarm(hour, minute, label)
                else:
                    print("Invalid time")
            except ValueError:
                print("Invalid input")
            input("\nPress Enter to continue...")
        elif choice == '2':
            clock.list_alarms()
            input("\nPress Enter to continue...")
        elif choice == '3':
            clock.list_alarms()
            try:
                index = int(input("\nAlarm number to delete: "))
                clock.delete_alarm(index)
            except ValueError:
                print("Invalid number")
            input("\nPress Enter to continue...")
        elif choice == '4':
            clock.list_alarms()
            try:
                index = int(input("\nAlarm number to toggle: "))
                clock.toggle_alarm(index)
            except ValueError:
                print("Invalid number")
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("\nUpcoming alarms:")
            current = datetime.datetime.now()
            upcoming = []
            
            for alarm in clock.alarms:
                if alarm["enabled"]:
                    alarm_dt = datetime.datetime.combine(current.date(), alarm["time"])
                    if alarm_dt > current:
                        upcoming.append((alarm_dt, alarm))
            
            if upcoming:
                for alarm_dt, alarm in sorted(upcoming):
                    time_left = alarm_dt - current
                    hours, remainder = divmod(time_left.seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    print(f"{alarm['time'].strftime('%H:%M')} - {alarm['label']} (in {hours}h {minutes}m)")
            else:
                print("No upcoming alarms")
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice")
            time.sleep(1)

# 42. ➗ GUI Calculator (Tkinter version)


if __name__ == "__main__":
    alarm_clock()
