#!/usr/bin/python3

"""
Documentation
"""


def canUnlockAll(boxes):

    """
    Method that determines if all the boxes can be opened
    """
    num_of_boxes = len(boxes)
    opened = [False] * num_of_boxes
    opened[0] = True
    keys = []

    print(opened)

    def get_keys(box):

        """
        Adds new keys to key list
        """
        for key in box:
            if key not in keys:
                keys.append(key)

    def checkBox(box):
        if opened[box]:
            return
        elif len(boxes[box]) and box in keys:
            opened[box] = True

    get_keys(boxes[0])

    for box in range(num_of_boxes):
        get_keys(boxes[box])
        checkBox(box)

    for box in range(num_of_boxes):
        get_keys(boxes[box])
        checkBox(box)

    print(opened)
    
    return all(opened)