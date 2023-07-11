# 전기가 부족해
# https://www.acmicpc.net/problem/10423

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
power_stations = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
# 부모 테이블에서 발전소들의 부모를 0으로 설정하여 하나의 집합으로 만들기
for p in power_stations:
    parent[p] = 0

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()  # 비용 순으로 정렬

result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
