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
                            unlockedBoxes.sort()
            else:
                unaccessed.append(index)
                # print('printUnaccessed', unaccessed)
        if unaccessed and (unaccessed != unaccessedBoxes):
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
    unlockedBoxes = []
    # print('locked boxes', lockedBoxes)
    # print('unlocked boxes', unlockedBoxes)
    # print(len(boxes))
    # exit()
    # print('locked boxes', lockedBoxes)
    # print('unlocked boxes', unlockedBoxes)
    unaccessedBoxes = []

    if lockedBoxes == []:
        return True

    for index, box in enumerate(boxes):
        # print("Index {}".format(index))
        for key in box:
            if index == 0 or index in unlockedBoxes:
                if key != 0 and key <= lockedBoxes[-1]:
                    if key not in unlockedBoxes:
                        unlockedBoxes.append(key)
                        unlockedBoxes.sort()
            else:
                unaccessedBoxes.append(index)
                break
        if unlockedBoxes == lockedBoxes:
            # print('unlocked boxes', unlockedBoxes)
            # print('no need to go further')
            return True

    # print('locked', lockedBoxes)
    # print('unlocked', unlockedBoxes)
    # print('reserve', unaccessedBoxes)

    checkUnaccessedBoxes(unaccessedBoxes, unlockedBoxes, lockedBoxes, boxes)

    # print('unlocked boxes', unlockedBoxes)
    # print('unlocked boxes', unlockedBoxes)
    if unlockedBoxes == lockedBoxes or len(lockedBoxes) == 0:
        return (True)
    return (False)
