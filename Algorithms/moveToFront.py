from __future__ import print_function

# contains all lowercase english symbol
SYMBOLTABLE = ['{}'.format(chr(x)) for x in range(128)]


def move2front_encode(filepath, symboltable):
    file = open(filepath, mode='r')
    free_exchange, access_cost, pad = 0,0, symboltable[:]
    while 1:
        char = file.read(1)
        if not char: break
        # print("{} - {}".format(repr(char), ord(char)))
        try:
            indx = pad.index(char)
            access_cost+=indx
            if indx!=0:
                free_exchange+=indx
            else:
                pass
            pad = [pad.pop(indx)] + pad
        except ValueError:
            print("{} - {}".format(repr(char), char))
    return free_exchange, access_cost


def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)

