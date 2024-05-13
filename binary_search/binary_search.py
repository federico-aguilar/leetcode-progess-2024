# Context:
# Given arr of int nums, sorted in ascending order 
# Given target to find

# Constraints:
# Algorithm must be O(log n) runtime complexity

# Returning:
# Target found, return idx
# Else return -1

# Scratch:
#
def search(nums,target):
    lft, rgt = 0, len(nums) - 1
    while lft <= rgt:
        mid = (rgt + lft) // 2 
        print(f"mid {mid} for lft {lft} & rgt {rgt}")
        if nums[mid] == target:
            return mid
        elif nums[mid] >= target:
            rgt = mid - 1
        else:
            lft = mid + 1
    return -1

if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 2))