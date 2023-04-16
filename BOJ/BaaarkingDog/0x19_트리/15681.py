# 트리와 쿼리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().split())  # 정점의 수, 루트, 쿼리의 수
graph = [[] for _ in range(N + 1)]
v = [0] * (N + 1)  # 서브트리에 속한 정점의 수를 담을 배열

for _ in range(N - 1):  # 그래프 연결
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(start):
    v[start] = 1
    for i in graph[start]:
        if not v[i]:
            dfs(i)
            v[start] += v[i]  # 자식 노드의 값을 부모 노드에 더해줌

dfs(R)  # 주어진 루트를 기준으로 dfs 수행

for _ in range(Q):
    print(v[int(input())])