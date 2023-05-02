import datetime
from playsound import playsound

alarm=input('Enter alarm time (in format HH:MM): ')

print('Alarm is set for: ',alarm)

while True:
    time=datetime.datetime.now()
    t=time.strftime('%H:%M')

    if t==alarm:
        print('its time')
        playsound('alarm.mp3')