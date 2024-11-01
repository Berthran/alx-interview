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
    i = 0
    if data is None:
        return False
    while i < len(data):
        # Get the codepoint
        codepoint = data[i]
        # Get the 8 least significant bits
        eightLSB = codepoint & 255

        # Check ASCII
        if eightLSB <= 127:
            # Ascii number: VALID
            i += 1
            continue

        # Check 2-Byte characters
        elif eightLSB >= 192 and eightLSB <= 223:
            # Check continuation Byte
            try:
                # In case continuation byte is not in the sequence
                nextContByte = data[i + 1]
                eightLSB = nextContByte & 255
                if eightLSB >= 128 and eightLSB <= 191:
                    i += 2
            except IndexError:
                return False

        # Check 3-Bytes Character
        elif eightLSB >= 224 and eightLSB <= 239:
            # Check continuation Bytes
            try:
                nextContByte1 = data[i + 1]
                eightLSB1 = nextContByte1 & 255
                if eightLSB1 >= 128 and eightLSB1 <= 191:
                    nextContByte2 = data[i + 2]
                    eightLSB2 = nextContByte2 & 255
                    if eightLSB2 >= 128 and eightLSB2 <= 191:
                        i += 3
                        continue
                    return False
                return False
            except IndexError:
                return False

        # Check 4-bytes Character
        elif eightLSB >= 240 and eightLSB <= 247:
            # Check continuation Bytes
            try:
                nextContByte1 = data[i + 1]
                eightLSB1 = nextContByte1 & 255
                if eightLSB1 >= 128 and eightLSB1 <= 191:
                    nextContByte2 = data[i + 2]
                    eightLSB2 = nextContByte2 & 255
                    if eightLSB2 >= 128 and eightLSB2 <= 191:
                        nextContByte3 = data[i + 3]
                        eightLSB3 = nextContByte3 & 255
                        if eightLSB3 >= 128 and eightLSB3 <= 191:
                            i += 4
                            continue
                        return False
                    return False
                return False
            except IndexError:
                return False
        else:
            return False
    return True
