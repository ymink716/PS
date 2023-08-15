# 택배
# https://www.acmicpc.net/problem/1719

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 최단 거리 테이블
route = [[0] * (n + 1) for _ in range(n + 1)]  # 집하장 경로 테이블

for i in range(1, n + 1):
    graph[i][i] = 0
    route[i][i] = INF

# 간선 정보 갱신
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    # a -> b 이면 b가 가장 먼저 거쳐야 할 집하장
    route[a][b] = b
    route[b][a] = a

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # k를 거쳐 가는 비용이 더 적다면
            if graph[a][b] > graph[a][k] + graph[k][b]:
                # 최단 거리 갱신
                graph[a][b] = graph[a][k] + graph[k][b]
                # 가장 먼저 거쳐야 할 집하장을 (a, k)의 집하장 값으로 갱신
                route[a][b] = route[a][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('-', end=" ")
        else:
            print(route[i][j], end=" ")
    print()