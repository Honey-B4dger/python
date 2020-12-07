import csv 
import os
import sys
import json
import time
from heatmap import Heatmap
from sudoku import Sudoku

files = [
        'easiest',
        'intermediate',
        #'difficult',
        'foo',
        'unsolvable',
        'not_fun',
        'wikipedia',
        ]

if __name__ == '__main__':

    exceptions = {}

    #nur starten, wenn auch wirklich dateien angegeben sind
    if files:
        for file in files:
            try:
                s = Sudoku(file, recording = True)
                s.solve()
                if s.exceptions:
                    exceptions[file] = s.exceptions

                h = Heatmap(file)
                h.plot_data()
            except:
                pass

        Sudoku.clear_terminal()
        print('Sequence completed!')
        print(f'\nThere has / have been {len(exceptions.keys())} exception(s) ', end = '')
        print('with the following file(s):')
        print('')

        for key, message in exceptions.items():
            print(f'\t- {key}: {message}')
        time.sleep(5)
    else:
        Sudoku.clear_terminal()
        print('No files specified. :(')
