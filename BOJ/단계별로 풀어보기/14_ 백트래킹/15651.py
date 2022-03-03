n, m = map(int, input().split())
visited = [False] * n
result = []

def solve(d, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        result.append(i + 1)
        solve(d + 1, n, m)
        result.pop()

solve(0, n, m)