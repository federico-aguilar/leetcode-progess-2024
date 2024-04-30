# def main():
from collections import deque
def car_fleet(target, position, speed):
    #iterate speed, and subtract by target to see how many miles to cover
    # then just divide by speed to see how many turns
    # this, is what you then sort
    combo = []
    for i in range(len(position)):
        combo.append([position[i], speed[i]])
    combo = sorted(combo, key=lambda x: x[0])
    moves = []
    for car in combo:
        pos, spd = car[0], car[1]
        distance = target - pos
        moves.append(distance // spd)
    stack = deque()
    fleets = 0
    for i in range(len(moves) - 1, -1, -1):
        broken = False
        while stack and moves[i] > stack[-1]:
            stack.pop()
            broken = True
        if broken is True:
            fleets += 1
        stack.append(moves[i])
    if stack:
        fleets += 1


if __name__ == "__main__":
    car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
