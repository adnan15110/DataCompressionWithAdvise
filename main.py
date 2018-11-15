from Algorithms.moveToFront import move2front_encode, move2front_decode, SYMBOLTABLE
from Algorithms.timeStamp import timestamp_encode
from Algorithms.contextBased import context_based_encode
import os

if __name__ == '__main__':
    CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir,'DataCompression','dataset', 'calgary'))
    print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))

    for file_name in ['book1','news','progc', 'trans']: # ,'news','progc', 'trans'
        PATH = os.path.abspath(os.path.join(CALGARY_DATASET_DIR, file_name))

        # free_exchange, access_cost = move2front_encode(PATH, SYMBOLTABLE)
        # print("MTF {} --> Free ex: {} AC: {}".format(file_name, free_exchange, access_cost))
        #
        #
        free_exchange, access_cost = timestamp_encode(PATH, SYMBOLTABLE)
        print("TS {} --> Free ex: {} AC: {}".format(file_name, free_exchange, access_cost))

        # free_exchange, access_cost = context_based_encode(PATH, SYMBOLTABLE)
        # print("CB {} --> Free ex: {} AC: {}".format(file_name, free_exchange, access_cost))