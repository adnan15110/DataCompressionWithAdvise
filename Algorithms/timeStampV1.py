from copy import deepcopy
from math import floor
import numpy as np
from pprint import pprint
import os


class TimeStampAlgorithm:
    def __init__(self, path, debug=False):
        """
        Initial setup for storage
        SYMBOLTABLE: holds all ascii char as a list in string representation.
        TIMESTAMP_DS: maintains the timestamp related information.
        INITIAL_DICT: a dictionary with each ascii char as key and their count as 0, requires when one a char is moves 
        the position, the algorithm uses this variable to initialize the TIMESTAMP_DS.
        """
        self.SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
        self.TIMESTAMP_DS = {}  # holds the time stamp related information.
        self.INITIAL_DICT = {'{}'.format(i): 0 for i in self.SYMBOLTABLE}
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
        """
        Reads a file and generate output file
        :return: 
        """
        file = open(self.INPUT_PATH, mode='r')
        pad = deepcopy(self.SYMBOLTABLE[:])

        while 1:
            try:
                char = file.read(1)
                if not char: break
                try:
                    char_list = self.timestamp_update(char)
                    indx = pad.index(char)
                    cost = indx + 1  # to account list index 0 as index 1
                    self.output['compressed size'] = self.output['compressed size'] + floor(2 * np.log(cost))
                    self.output['access cost'] += cost
                    self.output['standard cost'] += cost
                    self.output['MRM cost'] += cost
                    self.output['CC linear'] += cost
                    self.output['CC log'] = self.output['CC log'] + (1 + floor(2 * (np.log(cost))))

                    if char_list and len(char_list) > 0:
                        # here we have the time stamp list
                        swap_index = None
                        items_before_index = pad[:indx]
                        for ind, value in enumerate(items_before_index):
                            if value in char_list:
                                swap_index = ind
                                break

                        # insert the item in its position
                        if swap_index is not None:
                            if swap_index == 0:
                                self.output['free exchange'] = self.output['free exchange']+indx

                            # self.output['free exchange']+(indx-swap_index)

                            if self.DEBUG:
                                print("{} moved before {}".format(pad[indx], pad[swap_index]))

                            # pad[indx],pad[swap_index] = pad[swap_index], pad[indx]
                            v = pad.pop(indx)
                            pad = pad[:swap_index] + [v] + pad[swap_index:]
                            if self.DEBUG:
                                print("length of the list {}".format(len(pad)))
                    else:
                        pass
                except ValueError or IndexError:
                    self.output['skipped char'] += 1
                    if self.DEBUG:
                        print('Check the input file, unable to locate the char in the list')
            except UnicodeDecodeError:
                self.output['skipped char'] += 1
                if self.DEBUG:
                    print('Unicode error')

            self.output['compressed size'] = self.output['compressed size'] / 8
        return self.output

    def timestamp_update(self, char):
        """
        steps:
        1. checks whether char params exists in the key of TIMESTAMP_DS
            if exists 
              - pop the key and save the key to return and go to step 2
            else
              - this is first access
              - update all existing key's value
              - create new entry for this char

        2. Add the char to all existing key's value list
        3. Add char as key with [] value.
        :return: None if the value is there else None
        """
        char_list = None
        first_access = False

        if char in self.TIMESTAMP_DS:
            char_list = self.TIMESTAMP_DS.pop(char)
        else:
            first_access = True  # if it is the first access of the item

        # update all existing key's values for which the timestamp is available
        try:
            for key in self.TIMESTAMP_DS:
                if self.TIMESTAMP_DS[key][char]:
                    self.TIMESTAMP_DS[key][char] += 1
                    if self.TIMESTAMP_DS[key][char] > 1:
                        self.TIMESTAMP_DS[key].pop(char)
        except KeyError:
            print('already removed [{}]-[{}]'.format(key, char))

        # reset the time stamp if it is a second access or initialize the timestamp if it is the first access
        self.TIMESTAMP_DS[char] = {'{}'.format(i): 0 for i in self.SYMBOLTABLE}

        if char_list and not first_access:
            return list(char_list.keys())
        else:
            return []

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
        obj = TimeStampAlgorithm(path=PATH, debug=False)
        obj.encode()
        obj.report()
