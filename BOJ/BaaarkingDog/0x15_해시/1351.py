# 무한 수열
# https://www.acmicpc.net/problem/1351

n, p, q = map(int, input().split())

d = {}
d[0] = 1

def solve(n):
    if n in d:
        return d[n]

    d[n] = solve(n // p) + solve(n // q)

    return d[n]

print(solve(n))