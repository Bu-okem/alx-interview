#!/usr/bin/python3

"""
Documentation
"""


def canUnlockAll(boxes):

    """
    Method that determines if all the boxes can be opened
    """

    visited = [False] * len(boxes)
    visited[0] = True
    
    def unlockBox(box):
        if visited[box]:
            return
        
        visited[box] = True
        
        for key in boxes[box]:
            unlockBox(key)
    
    unlockBox(0)
    
    return all(visited)