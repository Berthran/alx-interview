#!/usr/bin/python3
'''
 a method that determines if all the boxes can be opened.

'''


def canUnlockAll(boxes):
    '''
    Returns True if all boxes can be opened
    '''
    # Index of the boxes locked -> first box is always opened
    locked = [i for i in range(len(boxes))][1:]
    # List to store unlocked boxes
    unlocked = []
    reserve = []
    
    for index, box in enumerate(boxes):
        for key in box:
            if index == 0:
                unlocked.append(key)
            else:
                if index in unlocked:
                    if (key != 0 and key <= locked[-1]) and (key not in unlocked):
                        unlocked.append(key)
                else:
                    reserve.append(index)
    reserve = list(set(reserve))

    for index in reserve:
        if index in unlocked:
            for key in boxes[index]:
                if index in unlocked and key != 0 and key <= locked[-1]:
                    if (key != 0 and key <= locked[-1]) and (key not in unlocked):
                        unlocked.append(key)
                

    unlocked.sort()
    if unlocked == locked:
        return (True)
    return (False)
