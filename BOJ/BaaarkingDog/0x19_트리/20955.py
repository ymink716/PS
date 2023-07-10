# 민서의 응급 수술
# https://www.acmicpc.net/problem/20955

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모를 자기 자신으로 초기화

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
for _ in range(m):  # 입력 받은 m개 간선에 대해
    u, v = map(int, input().split())
    # union 하기 전에 부모가 같다면 사이클이 존재함
    if find(parent, u) == find(parent, v):
        result += 1  # 사이클 제거 연산 +1
    else:  # 그게 아니면 유니온
        union(parent, u, v)

for i in range(1, n):
    # 다른 집합이라면 연결함
    if find(parent, i) != find(parent, i + 1):
        union(parent, i, i + 1)
        result += 1  # 연결하는 연산 +1

print(result)