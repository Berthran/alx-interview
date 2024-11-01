#!/usr/bin/python3
'''
Gets the unicode point of a character/grapheme
'''


def getUnicodePoint(char):
    return "U+{}".format(hex(ord(char))).replace('0x', '').upper()


char = "💜"
print(getUnicodePoint(char))
print(getUnicodePoint('丗'))
