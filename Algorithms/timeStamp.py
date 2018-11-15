SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]
TIMESTAMP_DS= {} # holds the time stamp related information.

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
    char_list=None
    if char in TIMESTAMP_DS:
        char_list=TIMESTAMP_DS.pop(char)

    for key in TIMESTAMP_DS:
        TIMESTAMP_DS[key].append(char)

    TIMESTAMP_DS[char]=[]

    return char_list


def  timestamp_decode():
    pass

