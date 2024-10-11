#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes1').canUnlockAll

if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    # print(boxes)

    print(canUnlockAll(boxes))
