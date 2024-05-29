# Content:
# Rows sorted increasing order
# First int of each row > last in of last row

# Contraints:
# Search in O(log(m*n))

# Returning:
# True if target exists, otherwise false

# Scratch:
# Run binary search on rows to find focus
# row to focus on is when target >= matrix[row][0] and target <= matrix[row][len(matrix[center]) - 1]

from typing import List


def search(matrix: List[int], target: int) -> int:
    top = 0
    bottom = len(matrix) - 1
    while top <= bottom:
        center = (bottom + top) // 2
        if target >= matrix[center][0] and target <= matrix[center][len(matrix[center]) - 1]:
            lft = 0
            rgt = len(matrix[center]) - 1
            while lft <= rgt:
                mid = (lft + rgt) // 2
                if target == matrix[center][mid]:
                    return True
                elif target < matrix[center][mid]:
                    rgt = mid - 1
                else:
                    lft = mid + 1
            return False
        elif target < matrix[center][0]:
            bottom = center - 1
        else:
            top = center + 1
        return False