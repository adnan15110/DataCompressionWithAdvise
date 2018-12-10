from __future__ import print_function
import numpy as np
from math import floor, log
from copy import deepcopy
from pprint import pprint
import os

class MoveToFront:
    """
    
    """

    def __init__(self, path,debug=False):
        """
        Initial setup for storage
        SYMBOLTABLE: holds all ascii char as a list in string representation.
        TIMESTAMP_DS: maintains the timestamp related information.
        INITIAL_DICT: a dictionary with each ascii char as key and their count as 0, requires when one a char is moves 
        the position, the algorithm uses this variable to initialize the TIMESTAMP_DS.
        """
        self.SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
        self.INPUT_PATH = path
        self.DEBUG = debug
        self.output = {
            'free exchange': 0,
            'access cost': 0,
            'standard cost': 0,
            'MRM cost': 0,
            'CC linear': 0,
            'CC log': 0,
            'compressed size': 0,
            'skipped char': 0  # >1 if any char skipped or not in ascii list
        }

    def encode(self):
        file = open(self.INPUT_PATH, mode='r')
        pad = deepcopy(self.SYMBOLTABLE[:])

        while 1:
            try:
                char = file.read(1)
                if not char: break
                # print("{} - {}".format(repr(char), ord(char)))
                try:
                    indx = pad.index(char)
                    cost = indx + 1
                    self.output['compressed size'] = self.output['compressed size'] + floor(2 * np.log(cost))
                    self.output['access cost'] += cost
                    self.output['standard cost'] += cost
                    self.output['MRM cost'] += cost
                    self.output['CC linear'] += cost
                    self.output['CC log'] = self.output['CC log'] + (1 + floor(2 * (np.log(cost))))

                    if indx > 0:
                        pad = [pad.pop(indx)] + pad
                        self.output['free exchange'] += indx + 1

                except ValueError:
                    self.output['skipped char'] += 1
                    if self.DEBUG:
                        print('Check the input file, unable to locate the char in the list')
            except UnicodeDecodeError:
                self.output['skipped char'] += 1
                if self.DEBUG:
                    print('Unicode error')
        return  self.output

    def decode(self):
        pass

    def report(self):
        """
        prints the output
        :return: 
        """
        pprint(self.output)

if __name__ == '__main__':
    CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir, 'dataset', 'calgary'))
    print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))

    for file_name in ['trans']:  # ,'news','progc', 'trans'
        PATH = os.path.abspath(os.path.join(CALGARY_DATASET_DIR, file_name))
        obj = MoveToFront(path=PATH, debug=False)
        obj.encode()
        obj.report()