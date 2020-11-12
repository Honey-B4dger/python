import math
import time
import os

degrees = 0

def print_bar(progress):

    remaining = (100 - progress)
    progress = progress

    print('[' + progress * '=' + remaining * '.' + ']', end = '\r')

os.system('clear')
while True:

    try:
        progress = int( 50 * math.sin(math.radians(degrees)) + 50)
        print_bar(progress)
        degrees += 5
        time.sleep(0.1)

        if degrees >= 360:
            degrees = 0

    except KeyboardInterrupt:
        break


