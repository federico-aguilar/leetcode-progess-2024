# Content:
# Originally get nums sorted in ascending order
# that has been rotated between 1 and n times.
# A rotation is shift of all ele idx pos o right by 1

# Contraints:
# nums has unique ele
# algo must run in O(log n)

# Returning:
# Min ele of arr

# Scratch:
# Find # of sorts?
# Can help identify min ele. How? 
# Tried and failed to find # of rotations.
# However, noticed pattern that if nums[mid] > nums [r], smallest in right section
# if nums[lft] > nums[mid], smallest in left section
# Initialize 2 pointers, lft  & rgt
# init smallest to + infinity
# while lft <= rgt, run conditions to check only sections where smallest can 'possibly' be in


def find_min(nums):
    lft = 0
    rgt = len(nums) - 1
    smallest = float('inf')
    while lft <= rgt:
        print()
        mid = (lft + rgt) // 2
        smallest = min(smallest, nums[mid])
        if nums[mid] > nums[rgt]:
            lft = mid + 1
        else:
            rgt = mid - 1
    print("runnign")
    return smallest

if __name__ == "__main__":
    print(find_min([4,5,6,7,0,1,2]))

# Runtime: 43 ms (beats 53.42%)
# Memory: 16.99 MB (beats 22.45%)
# TC: O(log n)
# SC: O(1)