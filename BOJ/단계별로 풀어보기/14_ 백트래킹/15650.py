n, m = map(int, input().split())
visited = [False] * n
result = []

def solve(d, s, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(s, n):
        if not visited[i]:
            visited[i] = True
            result.append(i + 1)
            solve(d + 1, i, n, m)
            visited[i] = False
            result.pop()

solve(0, 0, n, m)