import time
#from time import gmtime, strftime
import wave as sa

# TODO either repair references or delete app
path_to_file_start = 'c:\MEGA\Testing\pyfund\stopky\chimes_01.wav'
path_to_file_end = 'c:\MEGA\Testing\pyfund\stopky\Alarm09.wav'

wave_start = sa.openfp(path_to_file_start)
wave_end = sa.WaveObject.from_wave_file(path_to_file_end)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)            
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
    play_obj = wave_start.play()
    play_obj.wait_done()
