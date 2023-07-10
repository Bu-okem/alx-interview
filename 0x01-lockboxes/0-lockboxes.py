#!/usr/bin/python3

"""
Documentation
"""


def canUnlockAll(boxes):

    """
    Method that determines if all the boxes can be opened
    """
    num_of_boxes = len(boxes)
    opened = {0}  # Using a set for opened boxes
    keys = set(boxes[0])  # Using a set for keys

    def get_keys_from_box(box):
        keys.update(boxes[box])

    def check_box(box):

        """
        Opens box and gets the keys if it can be opened and isn't open
        """
        opened.add(box)
        get_keys_from_box(box)

    for box in range(num_of_boxes):
        while True:
            new_keys = set()
            for key in set(keys):  # Create a copy of keys before iterating
                if key not in opened:
                    check_box(key)
                    new_keys.update(boxes[key])
            keys.update(new_keys)
            if not new_keys:
                break

    return len(opened) == num_of_boxes