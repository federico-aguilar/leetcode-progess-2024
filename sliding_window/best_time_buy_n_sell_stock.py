# Content:

# Constraints:

# Returning:

# Scratch:

def max_profit(prices):
    # start w rgt @ end & lft = rgt - 1
    # while lft < rgt and lft = 0,
    max_profit = 0
    cheapest = float('inf')
    for price in prices:
        if price < cheapest:
            cheapest = min(cheapest, price)
        else:
            max_profit = max(max_profit, price - cheapest)
    return max_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))

# Runtime: 741 ms (beats 61.06%)
# Memory: 27.35 MB (beats 72.17%)
# TC: O(n)
# SC: 0(1)