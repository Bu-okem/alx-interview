#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))

boxes = [ [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6] ]
print(canUnlockAll(boxes))

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
