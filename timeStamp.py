from string import ascii_lowercase

SYMBOLTABLE = list(ascii_lowercase)

def timestamp_encode(strng, symboltable):
    symbol_call_list={}
    sequence, pad = [], symboltable[:]

    for char in strng:
        """
        First, check whether it is the first occurrence or not
        """

        indx = pad.index(char)
        sequence.append(indx)

        # maintain the timestamp
        if char in symbol_call_list.keys():
            symbol_call_list[char]=[]
        else:
            symbol_call_list[char]=[]

        for key, val in symbol_call_list.items():
            if key !=char:
                val.append(char)


        # decide whether we can move the item or not and if you need to move then find out
        # the index where the item should be inserted
        replace_index=None
        for ind, val in enumerate(pad[:indx]):
            if val in symbol_call_list.keys():
                if val in symbol_call_list[val]:
                    replace_index=ind
                    break

        if replace_index is not None:
            val = pad.pop(indx)
            pad.insert(replace_index, val)

    return sequence


def  timestamp_decode():
    pass

