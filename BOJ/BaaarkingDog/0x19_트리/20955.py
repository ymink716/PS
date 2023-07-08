# 민서의 응급 수술
# https://www.acmicpc.net/problem/20955

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(parent, u) == find(parent, v):
        result += 1
    union(parent, u, v)

for i in range(1, n):
    if find(parent, i) != find(parent, i + 1):
        union(parent, i, i + 1)
        result += 1

print(result)