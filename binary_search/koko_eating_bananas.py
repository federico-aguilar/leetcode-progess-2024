# Content:
# n piles of bananas, w ith pile having piles[i] bananas
# guards come back in h hours
# decide banana/hour eating SPEED of k
# Each hour, chooses pile and eats k bananas

# Contraints:
# If pile has less than k bananas, will eat them 
# all and stick around for completion of hour 
# and not even more
# piles.length >= 1
# h >= piles.length
# piles[i] > 1

# Returning:
# Return MINIMUM int k such that can eat all bananas within h hours

# Scratch: 
# 88 / 5 = 17.6 -> 18
import math

def koko_eating_bananas(piles, h):
    ft, rgt = 1, max(piles)
    munch = rgt
    while lft <= rgt:
        hours = 0
        k = (lft + rgt) // 2
        for pile in piles:
            hours += math.ceil(pile / k)
        if hours > h:
            lft = k + 1
        else:
            munch = min(munch, k)
            rgt = k - 1
    return munch
                

if __name__ == "__main__":
    print(koko_eating_bananas([30, 11, 23, 4, 20], 6))

# Runtime: 244 ms (beats 93.03%)
# Memory: 18.11 MB (beats 57.39%)
# TC: O(log n)
# SC: O(1)