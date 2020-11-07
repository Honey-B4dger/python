import math
import time

length = 10

def print_bar(progress, scale = 0.2):

    remaining = (100 - progress)
    progress = progress * scale

    #print(remaining, progress)

    print('|' + progress * '=' + remaining * ' ' + '|', end = '\r')

progress = 0


while True:
    try:
        progress += 1
        print_bar(progress)
        time.sleep(0.1)

        if progress >= 100:
            progress = 0
    except KeyboardInterrupt:
        break


