# Context:
# height has n vertical lines
# find two lines that together w x-axis form
# container, such that it contains most water

# Contraints:
# can't slant container 
# n >= 2 && n <= 10^5

# Returning:
# Maximum amount of water container can store

# Scratch:
# pointers @ each, while l < r
# get water between current l & r,
# bottleneck is shortest of two, 
# height[l] or height[r]
# then, move in the pointer @ the shortest
# when both pointers same height,
# move in whichever bc if smaller encountered
# due to move, that becomes bottleneck
# if bigger, the pointer that did not move
# becomes bottleneck

def three_sum(height):
    lft = 0
    rgt = len(height) - 1
    biggest_container = 0;
    while lft < rgt:
        container = (rgt - lft) * min(height[lft], height[rgt])
        biggest_container = max(biggest_container, container)
        if height[lft] < height[rgt]:
            lft += 1
        else:
            rgt -= 1
    return biggest_container



if __name__ == "__main__":
    print(three_sum([1, 1]))

# Runtime: 516 ms (beats 73.64%)
# Memory: 29.44 MB (beats 78.48%)