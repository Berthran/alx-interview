#!/usr/bin/python3
'''
 a method that determines if all the boxes can be opened.

'''


def checkUnaccessedBoxes(unaccessedBoxes, unlockedBoxes, lockedBoxes, boxes):
    if unaccessedBoxes:
        unaccessed = []

        for index in unaccessedBoxes:
            if index in unlockedBoxes:
                box = boxes[index]
                for key in box:
                    if key not in unlockedBoxes and key <= lockedBoxes[-1] \
                                                and key != 0:
                        unlockedBoxes.append(key)
                unlockedBoxes.sort()
            else:
                unaccessed.append(index)

        if unaccessed and (unaccessed != unaccessedBoxes):
            checkUnaccessedBoxes(unaccessed, unlockedBoxes, lockedBoxes, boxes)
        else:
            return unlockedBoxes

    else:
        return unlockedBoxes


def canUnlockAll(boxes):
    '''
    Returns True if all boxes can be opened
    '''
    lockedBoxes = [i for i in range(len(boxes))][1:]
    unlockedBoxes = []
    unaccessedBoxes = []

    # Empty box or box with only on
    if lockedBoxes == []:
        return True

    for index, box in enumerate(boxes):
        if index == 0 or index in unlockedBoxes:

            for key in box:
                if key not in unlockedBoxes and key <= lockedBoxes[-1] \
                                            and key != 0:
                    unlockedBoxes.append(key)
            unlockedBoxes.sort()

            if unlockedBoxes == lockedBoxes:
                # print('no need to go further')
                return True
        else:
            unaccessedBoxes.append(index)

    checkUnaccessedBoxes(unaccessedBoxes, unlockedBoxes, lockedBoxes, boxes)

    if unlockedBoxes == lockedBoxes:
        return (True)
    return (False)
