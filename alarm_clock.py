import sounddevice as sd
import soundfile as sf
import time
from datetime import datetime, timedelta

# ANSI (character or escape sequences)
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

alarms = []

def save_logs(alarm_logs):
    with open("logs.txt", "a") as file:
        file.write(alarm_logs + '\n')

def play_alarm_sound():
    data, fs = sf.read('alarm.wav.mp3')
    sd.play(data, fs)
    sd.wait()

def snooze_alarm(minutes=5):
    new_alarm = datetime.now() + timedelta(minutes=minutes)
    return new_alarm

def alarm(seconds):
    time_spent = 0

    print(CLEAR)

    while time_spent < seconds:
        time.sleep(1)
        time_spent += 1

        time_left = seconds - time_spent
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    
    current_time = datetime.now().strftime("%H:%M:%S")
    save_logs(f"Alarm got triggered at {current_time}")

    play_alarm_sound()

    choice = input("Press S to snooze for 5 min:")

    if choice.lower() == "s":
        snooze_time = snooze_alarm()

        print(f"Alarm snoozed till {snooze_time.strftime('%H:%M:%S')}")

        save_logs(f"Alarm snoozed till {snooze_time.strftime('%H:%M:%S')}")

        now = datetime.now()
        snooze_seconds = int((snooze_time - now).total_seconds())

        alarm(snooze_seconds)

num = int(input("Enter the number of alarms you want to set:"))

for i in range(num):
    print(f"Alarm {i+1} Timings")

    minutes = int(input("Enter the number of minutes:"))
    seconds = int(input("Enter the number of seconds:"))

    total_seconds = minutes*60 + seconds

    alarms.append(total_seconds)


for alarm_time in alarms:
    alarm(alarm_time)
