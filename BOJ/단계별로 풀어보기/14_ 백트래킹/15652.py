n, m = map(int, input().split())
result = []

def solve(d, s, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(s, n):
        result.append(i + 1)
        solve(d + 1, i, n, m)
        result.pop()

solve(0, 0, n, m)