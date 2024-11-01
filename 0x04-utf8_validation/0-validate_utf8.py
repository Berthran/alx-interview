#!/usr/bin/python3
'''
Validate if data is utf-8
'''


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
            i += 1     # Ascii grapheme: VALID
            continue

        # Check 2-Byte characters
        elif eightLSB >= 192 and eightLSB <= 223:
            # Check continuation Byte
            try:
                nextContByte = data[i + 1]
                eightLSB = nextContByte & 255
                if eightLSB >= 128 and eightLSB <= 191:
                    i += 2         # Valid Continuation Byte: VALID
                    continue
                return False       # Missing or Invalid Continuation Byte
            except IndexError:
                return False       # Missing Continuation Byte

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
                        i += 3        # Valid Continuation Bytes: VALID
                        continue
                    return False  # Missing/Invalid Second continuation Byte
                return False      # Missing/Invalid First continuation Byte
            except IndexError:
                return False      # Missing First Continuation Byte

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
                            i += 4      # Valid Continuation Bytes: VALID
                            continue
                        return False  # Missing/Invalid Third continuation Byte
                    return False    # Missing/Invalid Second continuation Byte
                return False        # Missing/Invalid First continuation Byte
            except IndexError:
                return False        # Missing First continuation Byte

        else:
            return False    # Invalid UTF-8 Encoding Pattern

    return True    # Valid UTF-8 Encoding Pattern
