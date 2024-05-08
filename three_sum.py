# Context:
# All unique triplets, where i != j != k
# nums[i] + nums[j] + nums[k]
# nums not ordered, random
# Order of output and order of triplets do not matter

# Constraints:
# 3 <= nums.length <= 3000

# Returning:
# [nums[i], nums[j], nums[k]]
# If none, return []

# Scratch:
#

def three_sum(nums):
    nums.sort()
    triplets = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        lft, rgt = i + 1, len(nums) - 1
        while lft < rgt:
            threesum = a + nums[lft] + nums[rgt]
            if threesum > 0:
                rgt -= 1
            elif threesum < 0:
                lft += 1
            else:
                triplets.append([a, nums[lft], nums[rgt]])
                lft += 1
                while nums[lft] == nums[lft - 1] and lft < rgt:
                    lft += 1
    return triplets

if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))

# Runtime: 633 ms (beats 78.28%)
# Memory: 20.77 MB (beats 52.74%)
