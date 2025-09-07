import time

alarm_time = input("Set alarm time (HH:MM): ")
print("Waiting for alarm...")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("⏰ Wake up!")
        break
    time.sleep(10)
