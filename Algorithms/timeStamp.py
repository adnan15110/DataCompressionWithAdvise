from copy import deepcopy
SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
TIMESTAMP_DS= {} # holds the time stamp related information.
INITIAL_DICT = {'{}'.format(i):0 for i in SYMBOLTABLE}

def timestamp_encode(filepath, symboltable):

    file = open(filepath, mode='r')
    free_exchange, access_cost, pad = 0, 0, symboltable[:]

    while 1:
        char = file.read(1)
        if not char: break
        try:
            indx = pad.index(char)
            access_cost+=indx
            char_list = timestamp_ds_update(char)
            if char_list and len(char_list)>0:
                # here we have the time stamp list we need to the list
                swap_index=None
                for ind,value in enumerate(pad[:indx]):
                    if value in char_list:
                        swap_index=ind
                        break

                # insert the item in its position
                if swap_index:
                    free_exchange+=1
                    # print("{} moved before {}".format(pad[indx], pad[swap_index]))
                    v = pad.pop(indx)
                    pad = pad[:swap_index]+ [v] + pad[swap_index:]
            else:
                pass
        except IndexError:
            print('Check the input file, unable to locate the char in the list')



    return free_exchange, access_cost


def timestamp_ds_update(char):
    """
    step:
    1. checks whether char params exists in the key of TIMESTAMP_DS
        if exists pop the key and save the key to return and go to step 2
        else proceed to step 2
    2. Add the char to all existing key's value list
    3. Add char as key with [] value.
    :return: None if the value is there else None
    """
    global TIMESTAMP_DS
    global INITIAL_DICT

    char_list=None
    if char in TIMESTAMP_DS:
        char_list=TIMESTAMP_DS.pop(char)

    try:
        for key in TIMESTAMP_DS:
            if TIMESTAMP_DS[key][char]:
                TIMESTAMP_DS[key][char]+=1
                if TIMESTAMP_DS[key][char]>1:
                    TIMESTAMP_DS[key].pop(char)
    except KeyError:
        print('{} -------- {}'.format(key, char))

    TIMESTAMP_DS[char]={'{}'.format(i):0 for i in SYMBOLTABLE}

    if char_list:
        return list(char_list.keys())
    else:
        return []


def  timestamp_decode():
    pass

