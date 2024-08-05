#!/usr/bin/python3

"""
Task 0
"""


def pascal_triangle(n):

        """
        returns list of lists of integers representing the Pascal’s triangle n
        """
        if n <= 0:
            return []

        triangle = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev_row = triangle[i - 1]
                    row.append(prev_row[j - 1] + prev_row[j])
            triangle.append(row)
        return triangle
