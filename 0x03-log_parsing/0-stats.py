#!/usr/bin/python3
'''
Parse log stats
'''
import sys
import signal


def handle_sigint(signum, frame):
    '''
    Handles CTRL+C
    '''
    filesize = frame.f_locals.get('totalfsize')
    statusCodes = frame.f_locals.get('statusCodes')
    print10logs(filesize, statusCodes)
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)


def print10logs(filesize, statusCodes):
    '''
    prints log report after 10 iteration
    '''
    print('File size: {}'.format(filesize))
    sortedscodes = sorted(statusCodes)
    print("\n".join("{}: {}".format(i, statusCodes[i])
                    for i in sortedscodes))


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
            print10logs(totalfsize, statusCodes)
            i = 0

    # lines = sys.stdin.read().splitlines()
    # for line in lines:
    #     print(f'[line {i+1}]', line)
    #     i += 1


if __name__ == "__main__":
    main()
