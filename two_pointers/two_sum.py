# Context:
# sorted in increasing order
# negative values are allowed

# Constraints:
# find two nums such that add up to specific target number
# exactly one solution, one pair of index values
# index values must be 1 indexed
# can't use same ele twice
# solution must use constant extra space, in-place

# Returning:
# index pair, 1-indexed

# Scratch:
# Think of pointer solution.. l r
# if addition of n[l] & n[r] != target, run changes
# if addition > target, decrease r //determine exactly by how much
# if addition < target, increase l // determine how much

def two_sum(nums, tar):
    lft = 0
    r = len(nums) - 1

    while lft < r:
        addition = nums[lft] + nums[r]
        if addition < tar:
            lft += 1
        elif addition > tar:
            r -= 1
        else:
            lft += 1
            r += 1
            return [lft, r]


if __name__ == "__main__":
    print(two_sum([2,7,11,12,15], 9))

# Runtime: 105 ms (beats 58%) O(n)
# Memory: 17.46 MB (beats 58%) O(1)
