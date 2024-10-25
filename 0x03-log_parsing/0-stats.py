#!/usr/bin/env python3
'''
Parse log stats
'''
import sys


def main():
    '''
    main program
    '''
    totalfsize = 0
    statusCodes = {}
    i = 0

    while True:
        i += 1
        line = sys.stdin.readline()
        if not line:
            break
        parts = line.strip('\n').split(' ')
        fsize = int(parts[-1])
        totalfsize += fsize

        try:
            scode = int(parts[-2])
            if (statusCodes.get(scode)):
                statusCodes[scode] += 1
            else:
                statusCodes[scode] = 1
        except Exception:
            pass

        if i == 10:
            print('File size: {}'.format(totalfsize))
            sortedscodes = sorted(statusCodes)
            print("\n".join("{}: {}".format(i, statusCodes[i])
                            for i in sortedscodes))
            i = 0

    # lines = sys.stdin.read().splitlines()
    # for line in lines:
    #     print(f'[line {i+1}]', line)
    #     i += 1


if __name__ == "__main__":
    main()
