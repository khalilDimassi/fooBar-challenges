import math

def count(area):
    if area == 1:
        return 1
    elif area > 1:
        x = (int(math.sqrt(area)) ** 2)
        return [x, count(area - x)]

def solution(area):
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
    solution= flatten(count(area))
    if None in solution:
        return [x for x in solution if x is not None]
    else:
        return solution
