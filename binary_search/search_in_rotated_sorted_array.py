# Content:
# originally, nums sorted in ascending order w distinct vals
# nums possibly rotated @ unknown pivot indx
# Given nums post-pivot

# Constraints:
# O(log n) runtime complexity

# Returning:
# return index of target if in nums or -1 if not in nums

# Scratch:
# 

def search(nums, target):
    lft = 0
    rgt = len(nums)
    while lft <= rgt:
        mid = (rgt + lft) // 2
        print(f"mid: {mid}")
        if nums[mid] == target:
            return mid
        if nums[lft] <= nums[mid]:
            if target > nums[mid] or target < nums[lft]:
                lft = mid + 1
            else:
                rgt = mid - 1
        else:
            if target < nums[mid] or target > nums[rgt]:
                rgt = mid - 1
            else:
                lft = mid + 1
    return -1
        

if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 1))

# Runtime: 51 ms (beats 8.75%)
# Memory: 17.06 MB (beats 17.06 MB)
# TC: O (log n)
# SC: O (1)