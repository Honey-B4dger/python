import os
import time
import re
import sys

def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    temp = re.search(r'(\d\d)\.\d', temp).group()
    return temp

while True:
    try:
        print(f'Aktuelle Kerntemperatur: {measure_temp()} °C')
        time.sleep(1)
    except KeyboardInterrupt:
        print('Temperatur-Monitor wird beendet...')
        sys.exit()

