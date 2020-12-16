import random
import time
import sys
import os
import copy
import csv
from snake import Snake

if __name__ == '__main__':
    iterations = 100
    results = []

    for iteration in range(iterations):
        log_attempt = {}
        s = Snake(10,10, erbose = False)
        s.main()
        print(f'\nIteration {iteration} / {iterations}')
        results.append(len(s.segments))

    av_length = round(sum(results)/len(results), 1)
    print(f'Average length over {len(results)} iterations: ', end = '')
    print(f'{av_length}')
