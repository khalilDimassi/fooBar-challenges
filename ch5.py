from bigO import BigO
from bigO import algorithm

lib = BigO()

def solution(l):
    if sum( n < 0 for n in l):
        return 0

    li = []

    for i_index, i in enumerate(l):
        for j_index, j in enumerate(l):
            for k_index, k in enumerate(l):
                try:
                    if (j % i == 0) and (k % j == 0) and (i_index < j_index) and (j_index < k_index) and (
                            i_index < k_index):
                        li.append((i, j, k))
                except ZeroDivisionError as E:
                    print(E)
                    return 0
    return len(li)

def solution_2(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            try:
                if l[i] % l[j] == 0:
                    c[i] += 1
                    count += c[j]
            except ZeroDivisionError as E:
                print(E)
                return 0
    return count

l = [1, 2, 0, 4, 5, 6]
l1 = [1, 1, 1]
print(solution(l))
print(solution_2(l))

