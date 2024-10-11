#!/usr/bin/python3
'''
 a method that determines if all the boxes can be opened.

'''


def canUnlockAll(boxes):
    '''
    Returns true if all boxes can be opened or else false
    '''

    if not boxes:
        return True # NO BOXES TO OPEN

    numOfBoxes = len(boxes)
    unlockedBoxes = {0}
    keys = set(boxes[0]) # No duplicate values

    while (keys):
        new_keys = set()
        for key in keys:
            if key not in unlockedBoxes and key < numOfBoxes:
                unlockedBoxes.add(key)
                new_keys.update(boxes[key])
        keys = new_keys - unlockedBoxes
    
    return len(unlockedBoxes) == numOfBoxes

        



