from collections import deque

def histogram(heights):
    # heights: List[int]
    # when current bar itself is bigger than smallest of previous times bar in row, 
    # erase the rest
    # initialize stack, smallest in stack, and largestArea
    # iterate heights
    # if height > smallest * len(stack), pop out all then set smallest to current height 
    # and add to stack
    # else, just add to stack while updating smallest by setting smallest = min(smallest, height)
    stack = deque()
    smallest = heights[0]
    largestArea = 0
    for height in heights:
        smallest = min(smallest, height)
        stack.append(height)
        while stack and height > smallest*len(stack):
            popped = stack.pop(0)
            smallest = min(popped, smallest)



if __name__ == "__main__":
    histogram([2,4])
