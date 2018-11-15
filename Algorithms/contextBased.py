from __future__ import print_function
from context_tree.context_tree import Trie, Queue
from functools import cmp_to_key
import os
# contains all lowercase english symbol
SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
CONTEXT_TREE = Trie()
C_MINUS_ONE_CONTEXT = None
C = 3
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
    file = open(filepath, mode='r')
    free_exchange, access_cost, pad = 0,0, symboltable[:]
    while 1:

        char = file.read(1)
        if not char: break
        try:
            #  step 1: linearly prob symboltable to find the index of x where x is the char
            indx = pad.index(char)
            access_cost+=indx

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
            if len(c_context)==3:
                global C_MINUS_ONE_CONTEXT
                C_MINUS_ONE_CONTEXT=c_context[1:]
                if C_MINUS_ONE_CONTEXT:
                    pad.sort(key=cmp_to_key(custom_comparator))
            else:
                pass
        except ValueError:
            print("{} - {}".format(repr(char), char))
    return free_exchange, access_cost


if __name__ == '__main__':
    CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir,'dataset', 'calgary'))
    print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))

    for file_name in ['book1']: # ,'news','progc', 'trans'
        PATH = os.path.abspath(os.path.join(CALGARY_DATASET_DIR, file_name))
        free_exchange, access_cost = context_based_encode(PATH, SYMBOLTABLE)
        print("CB {} --> Free ex: {} AC: {}".format(file_name, free_exchange, access_cost))