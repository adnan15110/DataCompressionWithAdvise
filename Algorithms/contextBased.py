from __future__ import print_function
from context_tree.context_tree import Trie, Queue
from functools import cmp_to_key
import os
import pickle
from math import floor
import numpy as np
from copy import deepcopy
# contains all lowercase english symbol
SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
C_MINUS_ONE_CONTEXT = None
C = 3
DEBUG = True
queue = Queue()

def custom_comparator(x, y):
    global C_MINUS_ONE_CONTEXT
    return recursive_comparator(x,y, C_MINUS_ONE_CONTEXT)

def recursive_comparator(x, y, context):
    global CONTEXT_TREE
    x_val = CONTEXT_TREE.search(context+[x])
    y_val = CONTEXT_TREE.search(context+[y])
    if x_val > y_val: # greater
        return 1
    elif x_val < y_val: #smaller
        return -1
    else: # equal
        # return 0
        if len(context)>1:
            return  recursive_comparator(x,y, context[1:])
        else:
            return 0

def bubble_sort(data, context):
    new_list=deepcopy(data)
    n = len(new_list)
    number_of_swap=0
    for i in range(n):
        for j in range(0, n - i - 1):
            j_val, j_1_val = get_context_value(new_list[j],new_list[j + 1], context)
            if j_val < j_1_val:
                number_of_swap+=1
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list, number_of_swap

def get_context_value(x,y, context):
    global CONTEXT_TREE
    x_val, y_val = CONTEXT_TREE.search(context + [x]), CONTEXT_TREE.search(context + [y])
    if x_val > y_val:  # greater
        return x_val, y_val
    elif x_val < y_val:  # smaller
        return x_val, y_val
    else:  # equal
        if len(context) > 1:
            return get_context_value(x, y, context[1:])
        else:
            return CONTEXT_TREE.search([x]), CONTEXT_TREE.search([y]) #single key search

def context_based_encode(filepath, symboltable):
    """
    Algorithms:
    step 1: linearly prob symboltable to find the index of x where x is the char
    step 2: update the context tree (c-1 items and x)
    step 3: rearrange pad based on (c-1) context
    
    :param filepath: 
    :param symboltable: 
    :return: 
    """
    global DEBUG
    working_on_byte=0
    file = open(filepath, mode='r')
    free_exchange, paid_exchange, access_cost, std_cost, mrm_cost, cc_linear, cc_log, pad, compressed_size = 0, 0, 0, 0, 0, 0, 0, symboltable[
                                                                                                                                 :], 0
    while 1:

        char = file.read(1)
        if not char: break
        working_on_byte+=1
        try:
            #  step 1: linearly prob symboltable to find the index of x where x is the char
            indx = pad.index(char)
            cost = indx + 1
            compressed_size = compressed_size + floor(2 * np.log(cost))
            access_cost += cost
            std_cost += cost
            mrm_cost += cost
            cc_linear += cost
            cc_log = cc_log + (1 + floor(2 * (np.log(cost))))

            #  step 2: update the context tree (c-1 items and x)
            if queue.size() < C:
                queue.enqueue(char)
            else:
                queue.dequeue()
                queue.enqueue(char)
            if queue.size() == C:
                global CONTEXT_TREE
                CONTEXT_TREE.insert(queue.getQueueData())

            # step 3: rearrange pad based on (c-1) context
            c_context = list(queue.getQueueData())
            if len(c_context)==C:
                global C_MINUS_ONE_CONTEXT
                C_MINUS_ONE_CONTEXT=c_context[1:]
                if C_MINUS_ONE_CONTEXT:
                    to_be_sorted_list = deepcopy(pad)
                    pad = sorted(to_be_sorted_list, key=cmp_to_key(custom_comparator))

                    # uncomment this code if the number of swap is required
                    # pad, number_of_swap = bubble_sort(pad, C_MINUS_ONE_CONTEXT)
                    # free_exchange+=number_of_swap #swaps are free
                    # print("{} - {} - number of swap {}".format(working_on_byte, char, number_of_swap))

                    print('sorted working on byte {}'.format(working_on_byte))
            else:
                pass
        except ValueError:
            print("{} - {}".format(repr(char), char))
    return free_exchange, access_cost, std_cost, mrm_cost, cc_linear, cc_log, floor(compressed_size / 8.0)


if __name__ == '__main__':
    CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir, 'dataset', 'calgary'))
    print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))

    for file_name in ['book1', 'news', 'progc','trans']: #
        CONTEXT_TREE = Trie()
        PATH = os.path.abspath(os.path.join(CALGARY_DATASET_DIR, file_name))
        free_exchange, access_cost, std_cost, mrm_cost, cc_linear, cc_log, size_in_byte = context_based_encode(PATH, SYMBOLTABLE)
        with open('{}.cb.advice'.format(file_name), 'wb') as f:
            pickle.dump(CONTEXT_TREE, f, pickle.HIGHEST_PROTOCOL)
        print("CB {} --> Free ex: {} AC: {} STD: {} MRM: {} cc_linear: {} cc_log:{} Compressed Size: {}".format(
            file_name, free_exchange, access_cost, std_cost, mrm_cost, cc_linear, cc_log, size_in_byte))
