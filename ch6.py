def solution(x, y):
    M, F = max(int(x), int(y)), min(int(x), int(y))
    res = 0
    while F > 0:
        res += M // F
        M, F = F, M % F
        print((M, F), res)
    if M != 1:
        return "impossible"
    return str(res - 1)

print(solution(5, 12))