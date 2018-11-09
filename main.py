from Algorithms.moveToFront import move2front_encode, move2front_decode, SYMBOLTABLE


if __name__ == '__main__':
    s='bananaaa'
    encode = move2front_encode(s, SYMBOLTABLE)
    print('%14r encodes to %r' % (s, encode), end=', ')
    decode = move2front_decode(encode, SYMBOLTABLE)
    print('which decodes back to %r' % decode)
    assert s == decode, 'Whoops!'