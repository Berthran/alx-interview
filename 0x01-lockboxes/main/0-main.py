#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes-set').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print("1", canUnlockAll(boxes))
print()

boxes = [[1]]
print(canUnlockAll(boxes))
print()

boxes = [[]]
print(canUnlockAll(boxes))
print()

boxes = [[1], [1], [2]]
print("4", canUnlockAll(boxes))
print()

boxes = [[1,2], [4], [5]]
print("5", canUnlockAll(boxes))
print()

boxes = [[2], [5], [1]]
print("6",canUnlockAll(boxes))
print()

boxes = [[1, 6], [2], [0, 1], [5, 6, 2], [3], [4, 1], [4]]
print("7", canUnlockAll(boxes))
print()

boxes = [[1, 4], [2], [0, 4, 1], [], [3], [0, 1, 6], [3, 5, 6]]
print("8",canUnlockAll(boxes))
print()
