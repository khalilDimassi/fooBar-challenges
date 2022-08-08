import numpy as np

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def lcmapp(lst):
    if len(lst) == 2:
        return lcm(lst[0], lst[1])
    else:
        return lcm(lst[0], lcmapp(lst[1:]))

def convertFracts(lst):
    denom = [i[1] for i in lst]
    ans = []
    lcm = lcmapp(denom)
    for i in range(len(lst)):
        ans.append([lcm/denom[i]*lst[i][0],lcm])
    return ans

def farey(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)
        if x == mediant:
            if b + d <= N:
                return a+c, b+d
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d

    if (b > N):
        return c, d
    else:
        return a, b

def input_to_transition(matrix):
    for i, row in enumerate(matrix):
        if sum(row) != 0:
            s = sum(row)
            for j, cell in enumerate(row):
                row[j] = cell / s
        else:
            row[i] = 1
    return matrix

def solution(input_matrix):
    transitionMatrix = input_to_transition(input_matrix)

    initial_vector = [1]
    initial_vector.extend([0 for _ in range(len(transitionMatrix) - 1)])
    s0 = np.array(initial_vector)

    x = []
    for _ in range(100):
        s0 = np.dot(s0, transitionMatrix)
        x = [float("{:.4f}".format(i)) for i in s0]

    y = convertFracts([farey(i, 100) for i in x])

    res = [int(i[0]) for i in y]
    res.append(int(y[0][1]))

    for index in range(len(input_matrix)):
        if input_matrix[index][index] != 1:
            res[index] = []

    for _ in range(len(res)):
        try:
            res.remove([])
        except ValueError as E:
            break

    return res

print()