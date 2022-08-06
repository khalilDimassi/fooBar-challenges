
def solution(l):
    list1 = [x.split('.') for x in l]
    list2 = sorted([list(map(int, y)) for y in list1])
    return ['.'.join(str(z) for z in a) for a in list2]