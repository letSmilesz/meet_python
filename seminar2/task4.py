# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник

import time

print('It`s timer.')
# hours = int(input('How many hours you want: '))
# minutes = int(input('How many minutes you want: '))
# seconds = int(input('How many seconds you want: '))
timer = input('Write time as format: HH:MM:SS \n')
all_times = timer.split(':')
seconds = int(all_times[2]) + int(all_times[1]) * 60 + (int(all_times[0]) * 60) * 60
for i in range(seconds):
    seconds_help = seconds
    hours = seconds_help // 60 // 60
    seconds_help -= hours * 60 * 60
    minutes = seconds_help // 60
    seconds_help -= minutes * 60
    print(f'{hours}:{minutes}:{seconds_help}')
    seconds -= 1
    time.sleep(1)