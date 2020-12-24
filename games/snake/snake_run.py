import random
import time
import sys
import os
import copy
import csv
from snake import *

if __name__ == '__main__':
    iterations = 2000
    results = []

    for iteration in range(iterations):
        log_attempt = {}
        s = Snake_circle(20,20, v = 'off', starve = False)
        s.main()
        print(f'\nIteration {iteration+1} / {iterations}')
        results.append(len(s.segments))

    av_length = round(sum(results)/len(results), 1)
    print(f'Average length over {len(results)} iterations: ', end = '')
    print(f'{av_length}')
