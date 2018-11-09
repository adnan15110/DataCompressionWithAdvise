import os
CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir,'dataset','calgary'))
print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))

PATH = os.path.abspath(os.path.join(CALGARY_DATASET_DIR,'book1'))
file = open(PATH, mode='r')

while 1:
    char = file.read(1)          # read by character
    if not char: break
    print("{} - {}".format(char, ord(char)))

file.close()