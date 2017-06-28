import time
import wave as sa
import pygame



# path_to_file_start = 'chimes_01.wav'
# path_to_file_end = 'Alarm09.wav'

# wave_start = sa.open(path_to_file_start)
# wave_end = sa.open(path_to_file_end)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1
    return 1
#    print('Goodbye!\n\n\n\n\n')

stop = False
lap = int(input('enter number of laps you wanna do: '))
cas = int(input('how much seconds each lap?: '))
while lap > 0:    
    print("Lap: ", lap, time.strftime('%X %x %Z'))
    lap -= countdown(cas)
    pygame.init()
    pygame.mixer.Sound('Alarm09.wav').play()
time.sleep(10)


