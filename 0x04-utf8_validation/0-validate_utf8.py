#!/usr/bin/python3
'''
Validate if data is utf-8
'''


def isascii(codepoint):
    '''
    Checks if a byte is an ascii character
    '''
    if codepoint >> 7 == 0:
        return True
    return False


def utf8range(codepoint):
    '''
    checks that a codepoint is in utf8range
    '''
    # Mask the first 8 bits of codepoint
    mask = (1 << 8) - 1
    if codepoint & mask <= 255:
        return True
    return False


def istwobytes(codepoint):
    pass


def isthreebytes(codepoint):
    pass


def isfoutbytes(codepoint):
    pass


def validUTF8(data):
    '''
    Checks if data is a valid UTF-8 encoding
    '''
    if data is None:
        return False
    for codepoint in data:
        if isascii(codepoint):
            continue
        else:
            return False
    return True
