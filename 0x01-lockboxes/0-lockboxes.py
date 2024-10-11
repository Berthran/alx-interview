#!/usr/bin/python3
'''
 a method that determines if all the boxes can be opened.

'''


def checkUnaccessedBoxes(unaccessedBoxes, unlockedBoxes, lockedBoxes, boxes):
    if unaccessedBoxes:
        unaccessed = []
        # print("Calling")
        for index in unaccessedBoxes:
            # print('index', index)
            if index in unlockedBoxes:
                # print('index {} accessed'.format(index))
                for key in boxes[index]:
                    if key != 0 and key <= lockedBoxes[-1]:
                        if (key not in unlockedBoxes):
                            unlockedBoxes.append(key)
            else:
                unaccessed.append(index)
                # print('printUnaccessed', unaccessed)
        if unaccessed and (len(unaccessed) < len(unaccessedBoxes)):
            # print('Going back for', unaccessed)
            checkUnaccessedBoxes(unaccessed, unlockedBoxes, lockedBoxes, boxes)
        else:
            # print('unlocked boxes after recursion', unlockedBoxes)
            # print('Done with recursion')
            # print(f'returning {unlockedBoxes} of type {type(unlockedBoxes)}')
            return unlockedBoxes
    else:
        # print('unlocked boxes no recursion', unlockedBoxes)
        # print('No recursion')
        return unlockedBoxes


def canUnlockAll(boxes):
    '''
    Returns True if all boxes can be opened
    '''
    lockedBoxes = [i for i in range(len(boxes))][1:]
    unlockedBoxes = [key for key in boxes[0]]
    unaccessedBoxes = []

    for index, box in enumerate(boxes[1:], start=1):
        for key in box:
            if index in unlockedBoxes:
                if key != 0 and key <= lockedBoxes[-1]:
                    if key not in unlockedBoxes:
                        unlockedBoxes.append(key)
            else:
                unaccessedBoxes.append(index)
                break

    # print('locked', lockedBoxes)
    # print('unlocked', unlockedBoxes)
    # print('reserve', unaccessedBoxes)

    checkUnaccessedBoxes(unaccessedBoxes, unlockedBoxes, lockedBoxes, boxes)

    unlockedBoxes.sort()
    if unlockedBoxes == lockedBoxes:
        return (True)
    return (False)
