# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник

import time
import pyglet

print('It`s timer.')
timer = input('Write time as format: HH:MM:SS \n')
time_str = timer.split(':')
all_times = []
for i in time_str:
    all_times.append(int(i))
song = pyglet.media.load('C:/Users/User/Код/letSmilesz/MeetPython/seminar2/alarm.mp3')

#option 2
for i in range(all_times[0], -1, -1):
    for j in range(all_times[1], -1, -1):
        for l in range(all_times[2], -1, -1):
            if (i ==0 and j == 0) and l == 0: 
                song.play()
                pyglet.app.run()
            else:
                print(f'{i}:{j}:{l}')
                time.sleep(1)
            all_times[2] -= 1
        all_times[1] -= 1
        all_times[2] += 60
    all_times[0] -= 1
    all_times[1] += 60

#option 1
#seconds = int(all_times[2]) + int(all_times[1]) * 60 + (int(all_times[0]) * 60) * 60

# for i in range(seconds):
#     seconds_help = seconds
#     hours = seconds_help // 60 // 60
#     seconds_help -= hours * 60 * 60
#     minutes = seconds_help // 60
#     seconds_help -= minutes * 60
#     print(f'{hours}:{minutes}:{seconds_help}')
#     seconds -= 1
#     time.sleep(1)

