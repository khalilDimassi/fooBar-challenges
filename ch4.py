import random


def define_probs(matrix):
    all_prob = []
    i = 0
    while i < len(matrix):
        p = []
        for index, elem in enumerate(matrix[i]):
            if elem != 0:
                p.extend([(elem, index, i) for _ in range(elem)])
        all_prob.append(p)
        i += 1
    return all_prob


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


def simulate(matrix, iteration):
    probs = define_probs(matrix)
    termios = {j: 0 for j in range(len(matrix)) if sum(matrix[j]) == 0}
    for _ in range(iteration):
        i = 0
        while i < len(matrix):
            x = random.choice(probs[i])
            if sum(matrix[x[1]]) != 0:
                i = x[1]
            else:
                termios[x[1]] += 1
                break
    return termios

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

def solution(matrix):
    termios = simulate(matrix, 1000000)
    print(termios)

    sol = convertFracts([farey(i*0.000001, 100) for i in termios.values()])
    ution = [int(i[0]) for i in sol]
    ution.append(int(sol[0][1]))
    return ution
