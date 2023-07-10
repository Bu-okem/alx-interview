#!/usr/bin/python3

"""
Documentation
"""


# def canUnlockAll(boxes):

#     """
#     Method that determines if all the boxes can be opened
#     """
#     num_of_boxes = len(boxes)
#     opened = [False] * num_of_boxes
#     opened[0] = True
#     keys = []


#     def get_keys(box):

#         """
#         Adds new keys to key list
#         """
#         for key in box:
#             if key not in keys:
#                 keys.append(key)

#     def checkBox(box):

#         """
#         Opens box and gets the keys if it can be opened and isn't open
#         """
#         if opened[box]:
#             return
#         elif box in keys:
#             opened[box] = True
#             get_keys(boxes[box])

#     get_keys(boxes[0])

#     for box in range(num_of_boxes):
#         checkBox(box)

#     for box in range(num_of_boxes):
#         checkBox(box)
    
#     return all(opened)

def canUnlockAll(boxes):
    num_of_boxes = len(boxes)
    opened = {0}  # Using a set for opened boxes
    keys = set(boxes[0])  # Using a set for keys

    def get_keys_from_box(box):
        keys.update(boxes[box])

    def check_box(box):
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