import math

def solution(n, m):
    return [math.gcd(n, m), int(n * m / math.gcd(n, m))]


# test
print(solution(3, 12))
print(solution(2, 5))